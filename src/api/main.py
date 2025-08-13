#!/usr/bin/env python3
"""
OpsAI FastAPI Main Application

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module contains the main FastAPI application for OpsAI,
providing AI-powered ticket classification and resolution.
"""

import os
import pickle
import json
from typing import List

import faiss
import torch
from fastapi import FastAPI

from pydantic import BaseModel, Field
from sentence_transformers import SentenceTransformer
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
)
from transformers.utils.quantization_config import BitsAndBytesConfig
from transformers.generation.configuration_utils import GenerationConfig
from peft import PeftModel
from src.monitoring.metrics import setup_metrics
from src.integrations.jira import router as jira_router

import sqlite3
from pathlib import Path


DB_PATH = Path("data") / "opsai.db"
DB_PATH.parent.mkdir(exist_ok=True)


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
      CREATE TABLE IF NOT EXISTS feedback (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket    TEXT NOT NULL,
        suggestion TEXT NOT NULL,
        rating    INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
        comment   TEXT,
        ts        DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    """)
    conn.commit()
    conn.close()


# ─── Configuration ─────────────────────────────────────────────────────
INDEX_DIR = os.getenv("INDEX_DIR", "data/index")
ADAPTER_DIR = os.getenv("ADAPTER_DIR", "models/lora_adapter")
BASE_MODEL = os.getenv("BASE_MODEL", "EleutherAI/gpt-neo-125M")
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
TOP_K_DEFAULT = int(os.getenv("TOP_K", "3"))

# ─── Load vector index & metadata ──────────────────────────────────────
_index_path = os.path.join(INDEX_DIR, "ticket_index.faiss")
_meta_path = os.path.join(INDEX_DIR, "ticket_meta.pkl")
_index = faiss.read_index(_index_path)
_meta = pickle.load(open(_meta_path, "rb"))

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
init_db()
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


class FeedbackIn(BaseModel):
    ticket: dict
    suggestion: str
    rating: int = Field(ge=1, le=5)
    comment: str | None = None


# simple mapping of labels → team names (adjust as needed)
LABEL_TEAM_MAP = {
    "network": "IT Helpdesk",
    "auth": "IT Helpdesk",
    "performance": "Engineering",
    "mail": "IT Helpdesk",
    "tooling": "Engineering",
    "user": "IT Helpdesk",
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

    # Tokenize and move to the same device as the model
    inputs = _tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    # Move input tensors to the same device as the model
    device = next(_model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Use proper generation parameters (remove temperature as it's causing issues)
    gen_cfg = GenerationConfig(
        max_new_tokens=100,
        do_sample=True,
        top_p=0.9,
        pad_token_id=_tokenizer.eos_token_id
    )

    with torch.no_grad():
        out = _model.generate(**inputs, generation_config=gen_cfg)

    suggestion = _tokenizer.decode(out[0], skip_special_tokens=True)[len(prompt):].strip()

    return {"suggestion": suggestion, "context_tickets": [h["ticket"] for h in hits]}


@app.post("/feedback")
async def feedback(data: FeedbackIn):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO feedback (ticket, suggestion, rating, comment) VALUES (?, ?, ?, ?)",
        (json.dumps(data.ticket), data.suggestion, data.rating, data.comment),
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}
