#!/usr/bin/env python3
"""
Ingestion Testing Module for OpsAI
Unit tests for data ingestion pipeline and ticket processing.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# tests/test_ingestion.py
import os
import json
import pytest
from src.ingestion.parser import normalize_ticket
from src.ingestion.ingest import main as ingest_main


@pytest.fixture
def sample_data(tmp_path):
    raw = tmp_path / "raw"
    out = tmp_path / "processed"
    raw.mkdir()
    out.mkdir()
    # create a small CSV
    csv_file = raw / "tickets.csv"
    csv_file.write_text(
        "Subject,Description,Tags,Resolution\n"
        "VPN down,Can't connect to VPN.,network,Restart VPN service\n"
    )
    # create a small JSON
    json_file = raw / "tickets.json"
    json_file.write_text(
        json.dumps([{
            "title": "Reset pwd",
            "body": "Forgot my password",
            "labels": ["auth","user"],
            "resolution": "Password reset link sent"
        }])
    )
    return str(raw), str(out)


def test_ingest_creates_files(sample_data):
    raw, out = sample_data
    # run ingestion
    ingest_main(raw, out)
    files = sorted(os.listdir(out))
    assert files == ["ticket_0.json", "ticket_1.json"]
    # verify content
    with open(os.path.join(out, files[0]), 'r', encoding='utf-8') as f:
        t0 = json.load(f)
    assert normalize_ticket(t0)['title'] == "VPN down"
    with open(os.path.join(out, files[1]), 'r', encoding='utf-8') as f:
        t1 = json.load(f)
    assert normalize_ticket(t1)['labels'] == ["auth", "user"]
