#!/usr/bin/env python3
"""
Embeddings Testing Module for OpsAI
Unit tests for vector embeddings, FAISS indexing, and semantic search.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# tests/test_embeddings.py

import os
import json
import tempfile
from src.embeddings.embedder     import build_and_save
from src.embeddings.retriever    import load_index, query_index

def test_embedding_and_retrieval(tmp_path):
    # 1) Create a fake processed directory
    proc_dir = tmp_path / "processed"
    idx_dir  = tmp_path / "index"
    proc_dir.mkdir()
    idx_dir.mkdir()

    tickets = [
        {"title": "VPN down", "body": "Cannot connect to VPN", "labels": [], "resolution": ""},
        {"title": "Email error", "body": "SMTP server unreachable", "labels": [], "resolution": ""}
    ]
    # Write two JSONs
    for i, t in enumerate(tickets):
        with open(proc_dir / f"ticket_{i}.json", "w", encoding="utf-8") as f:
            json.dump(t, f)

    # 2) Build index
    build_and_save(str(proc_dir), str(idx_dir), model_name="all-MiniLM-L6-v2")

    # 3) Load and query
    ix, meta = load_index(str(idx_dir) + "/ticket_index.faiss",
                          str(idx_dir) + "/ticket_meta.pkl")
    results = query_index("VPN", ix, meta, model_name="all-MiniLM-L6-v2", top_k=1)
    assert len(results) == 1
    assert "VPN" in results[0]["ticket"]["title"]
