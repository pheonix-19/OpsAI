#!/usr/bin/env python3
"""
OpsAI Vector Index Builder

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module builds FAISS vector indexes for semantic search.
"""

import argparse
from .embedder import build_and_save


def main():
    parser = argparse.ArgumentParser(description="Build FAISS index over processed tickets")
    parser.add_argument('--input-dir', required=True, help="Directory of processed JSON tickets")
    parser.add_argument('--output-dir', required=True, help="Where to save the FAISS index + meta")
    parser.add_argument('--model', default='all-MiniLM-L6-v2', help="SentenceTransformer model")
    args = parser.parse_args()

    build_and_save(args.input_dir, args.output_dir, args.model)


if __name__ == '__main__':
    main()
