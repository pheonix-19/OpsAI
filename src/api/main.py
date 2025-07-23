# src/api/main.py

import os
import pickle
from typing import List

import faiss
import torch
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    GenerationConfig,
)
from peft import PeftModel
from src.monitoring.metrics import setup_metrics
from src.integrations.jira import router as jira_router


# ─── Configuration ─────────────────────────────────────────────────────
INDEX_DIR     = os.getenv("INDEX_DIR", "data/index")
ADAPTER_DIR   = os.getenv("ADAPTER_DIR", "models/lora_adapter")
BASE_MODEL    = os.getenv("BASE_MODEL", "EleutherAI/gpt-neo-125M")
EMBED_MODEL   = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
TOP_K_DEFAULT = int(os.getenv("TOP_K", "3"))

# ─── Load vector index & metadata ──────────────────────────────────────
_index_path = os.path.join(INDEX_DIR, "ticket_index.faiss")
_meta_path  = os.path.join(INDEX_DIR, "ticket_meta.pkl")
_index = faiss.read_index(_index_path)
_meta  = pickle.load(open(_meta_path, "rb"))

# ─── Load sentence‐transformer for embeddings ─────────────────────────
_embedder = SentenceTransformer(EMBED_MODEL)

# ─── Load LoRA‑fine‑tuned LLM ──────────────────────────────────────────
# 1) load base model quantized for CPU/GPU
bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)
_base = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=bnb_cfg,
    device_map="auto",
)
# 2) wrap with the adapter
_model = PeftModel.from_pretrained(_base, ADAPTER_DIR, device_map="auto")
_tokenizer = AutoTokenizer.from_pretrained(ADAPTER_DIR, use_fast=True)
# ensure pad token is set
if _tokenizer.pad_token is None:
    _tokenizer.pad_token = _tokenizer.eos_token
    _tokenizer.pad_token_id = _tokenizer.eos_token_id

# ─── FastAPI app & schemas ─────────────────────────────────────────────
app = FastAPI(title="OpsAI Inference API")
setup_metrics(app)
app.include_router(jira_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the OpsAI API! See /docs for usage."}

class QueryPayload(BaseModel):
    text: str
    top_k: int = TOP_K_DEFAULT

class ClassifyResponse(BaseModel):
    tags: List[str]
    teams: List[str]

class ResolveResponse(BaseModel):
    suggestion: str
    context_tickets: List[dict]

# simple mapping of labels → team names (adjust as needed)
LABEL_TEAM_MAP = {
    "network":    "IT Helpdesk",
    "auth":       "IT Helpdesk",
    "performance":"Engineering",
    "mail":       "IT Helpdesk",
    "tooling":    "Engineering",
    "user":       "IT Helpdesk",
}

def _retrieve(text: str, top_k: int):
    q_emb = _embedder.encode([text], convert_to_numpy=True)
    dists, idxs = _index.search(q_emb, top_k)
    results = []
    for dist, idx in zip(dists[0], idxs[0]):
        path = _meta["ticket_paths"][idx]
        ticket = pickle.load(open(path.replace(".json", ".pkl"), "rb")) \
                 if path.endswith(".pkl") else __import__("json").load(open(path))
        results.append({"ticket": ticket, "distance": float(dist)})
    return results

@app.post("/classify", response_model=ClassifyResponse)
async def classify(q: QueryPayload):
    hits = _retrieve(q.text, q.top_k)
    # collect tags from neighbors
    tag_counts = {}
    for h in hits:
        for tag in h["ticket"].get("labels", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    # sort by frequency
    tags = sorted(tag_counts, key=lambda t: -tag_counts[t])
    # map to teams
    teams = sorted({LABEL_TEAM_MAP.get(tag, "Other") for tag in tags})
    return {"tags": tags, "teams": teams}

@app.post("/resolve", response_model=ResolveResponse)
async def resolve(q: QueryPayload):
    hits = _retrieve(q.text, q.top_k)
    # build a RAG context
    contexts = []
    for h in hits:
        t = h["ticket"]
        contexts.append(f"- {t['title']}: {t['resolution']}")
    context_str = "\n".join(contexts)

    # construct prompt
    prompt = (
        "You are an AI assistant for IT support. "
        "Given these past tickets and resolutions:\n"
        f"{context_str}\n\n"
        f"New ticket: {q.text}\n"
        "Provide a concise resolution suggestion:"
    )

    inputs = _tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    gen_cfg = GenerationConfig(max_new_tokens=100, temperature=0.2)
    out = _model.generate(**inputs, generation_config=gen_cfg)
    suggestion = _tokenizer.decode(out[0], skip_special_tokens=True)[len(prompt):].strip()

    return {"suggestion": suggestion, "context_tickets": [h["ticket"] for h in hits]}
