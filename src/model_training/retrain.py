#!/usr/bin/env python3
"""
Model Retraining Module for OpsAI
Automated retraining pipeline for LoRA fine-tuning with continuous learning.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# src/model_training/retrain.py

import argparse
from datetime import datetime
from train_lora import main as train_main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument("--base-model", default="EleutherAI/gpt-neo-125M")
    parser.add_argument("--output-dir", default=None,
                        help="If unset, writes to models/adapters/YYYYMMDD_HHMM")
    parser.add_argument("--epochs", type=int, default=1)
    args = parser.parse_args()

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M")
    out = args.output_dir or f"models/adapters/{ts}"
    train_main([
        "--data-dir", args.data_dir,
        "--base-model", args.base_model,
        "--output-dir", out,
        "--epochs", str(args.epochs),
        "--batch-size", "4",
        "--max-length", "512",
        "--learning-rate", "3e-4",
    ])
    print(f"Retrained adapter saved to {out}")
