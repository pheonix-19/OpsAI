#!/usr/bin/env python3
"""
OpsAI Embedding Generator

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module handles text embedding generation and FAISS index operations.
"""

import os
import json
import pickle
from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss


def load_tickets(input_dir: str) -> List[Dict]:
    """
    Load all JSON tickets from input_dir and return as a list of dicts.
    """
    tickets = []
    # Use sorted so order is deterministic
    for fname in sorted(os.listdir(input_dir)):
        if fname.endswith('.json'):
            with open(os.path.join(input_dir, fname), 'r', encoding='utf-8') as f:
                tickets.append(json.load(f))
    return tickets


def embed_tickets(tickets: List[Dict], model_name: str = 'all-MiniLM-L6-v2') -> np.ndarray:
    """
    Embed each ticket by concatenating title + body.
    Returns an (N × D) numpy array.
    """
    model = SentenceTransformer(model_name)
    texts = [t['title'] + ' ' + t['body'] for t in tickets]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    return embeddings


def build_faiss_index(embeddings: np.ndarray):
    """
    Build a simple L2 FAISS index over the embeddings.
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_index(index, index_path: str, meta: Dict, meta_path: str):
    """
    Persist the FAISS index and metadata (ticket_paths) to disk.
    """
    faiss.write_index(index, index_path)
    with open(meta_path, 'wb') as f:
        pickle.dump(meta, f)


def build_and_save(input_dir: str, output_dir: str, model_name: str = 'all-MiniLM-L6-v2'):
    """
    Load tickets, embed them, build FAISS index, and save index + metadata.
    """
    tickets = load_tickets(input_dir)
    embeddings = embed_tickets(tickets, model_name)
    index = build_faiss_index(embeddings)

    # Prepare metadata: full paths to each JSON file, in the same order as embeddings
    ticket_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.json')])
    ticket_paths = [os.path.join(input_dir, f) for f in ticket_files]
    meta = {'ticket_paths': ticket_paths}

    os.makedirs(output_dir, exist_ok=True)
    index_path = os.path.join(output_dir, 'ticket_index.faiss')
    meta_path = os.path.join(output_dir, 'ticket_meta.pkl')
    save_index(index, index_path, meta, meta_path)

    print(f"[✅] Built index with {embeddings.shape[0]} vectors → {output_dir}")
