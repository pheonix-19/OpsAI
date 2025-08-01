#!/usr/bin/env python3
"""
Model Training Testing Module for OpsAI
Unit tests for LoRA fine-tuning and model training pipeline.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# tests/test_model_training.py

import os
import json
import tempfile
from src.model_training.train_lora import TicketDataset
from transformers import AutoTokenizer

def test_ticket_dataset(tmp_path):
    # prepare a processed ticket
    proc = tmp_path / "processed"
    proc.mkdir()
    sample = {
        "title": "VPN error",
        "body": "Cannot connect to VPN gateway",
        "labels": ["network"],
        "resolution": "Restart VPN service"
    }
    (proc / "ticket_0.json").write_text(json.dumps(sample))

    # init tokenizer & dataset
    tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True)
    ds = TicketDataset(str(proc), tokenizer, max_length=32)

    # one sample, correct fields
    assert len(ds) == 1
    item = ds[0]
    assert set(item.keys()) == {"input_ids", "attention_mask", "labels"}
    # labels should have -100 for prompt tokens
    prompt_ids = tokenizer("Ticket: VPN error Cannot connect to VPN gateway Solution:", add_special_tokens=False).input_ids
    assert (item["labels"][:len(prompt_ids)] == -100).all()
