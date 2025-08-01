#!/usr/bin/env python3
"""
OpsAI Vector Retriever

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module handles semantic search and vector retrieval operations.
"""

import os
import pickle
import argparse
import json
from sentence_transformers import SentenceTransformer
import faiss

def load_index(index_path: str, meta_path: str):
    """
    Load FAISS index and metadata (ticket_paths) from disk.
    """
    index = faiss.read_index(index_path)
    with open(meta_path, 'rb') as f:
        meta = pickle.load(f)
    return index, meta

def query_index(query: str, index, meta, model_name: str, top_k: int):
    """
    Embed the query, search the FAISS index, and return top_k tickets with distances.
    """
    model = SentenceTransformer(model_name)
    q_emb = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_emb, top_k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        ticket_path = meta['ticket_paths'][idx]
        ticket = json.load(open(ticket_path, 'r', encoding='utf-8'))
        results.append({
            'ticket':   ticket,
            'distance': float(dist)
        })
    return results

def main():
    parser = argparse.ArgumentParser(description="Query the ticket FAISS index")
    parser.add_argument('--query',     required=True, help="Text query")
    parser.add_argument('--index-dir', required=True, help="Directory with ticket_index.faiss & ticket_meta.pkl")
    parser.add_argument('--input-dir',  required=False, help="(Not used) kept for symmetry")
    parser.add_argument('--model',      default='all-MiniLM-L6-v2', help="SentenceTransformer model")
    parser.add_argument('--top-k',      type=int, default=5, help="How many results to return")
    args = parser.parse_args()

    ix = os.path.join(args.index_dir, 'ticket_index.faiss')
    mt = os.path.join(args.index_dir, 'ticket_meta.pkl')
    index, meta = load_index(ix, mt)
    results = query_index(args.query, index, meta, args.model, args.top_k)
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
