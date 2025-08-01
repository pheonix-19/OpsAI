#!/usr/bin/env python3
"""
API Testing Module for OpsAI
Unit tests for FastAPI endpoints and AI operations functionality.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# tests/test_api.py

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_classify_and_resolve(monkeypatch, tmp_path):

    # monkeypatch retrieval to return fixed tickets
    fake_tickets = [
        {"title": "VPN down", "body": "...", "labels": ["network"], "resolution": "Restart VPN."},
        {"title": "Email fail", "body": "...", "labels": ["mail"], "resolution": "Check SMTP."},
    ]

    def fake_retrieve(text, top_k):
        return [{"ticket": t, "distance": 0.0} for t in fake_tickets]
    monkeypatch.setattr("src.api.main._retrieve", fake_retrieve)

    # test classify
    res = client.post("/classify", json={"text":"VPN issue","top_k":2})
    data = res.json()
    assert res.status_code == 200
    assert "network" in data["tags"]
    assert "IT Helpdesk" in data["teams"]

    # test resolve
    res2 = client.post("/resolve", json={"text":"VPN issue","top_k":2})
    data2 = res2.json()
    assert res2.status_code == 200
    assert "Restart VPN." in data2["suggestion"]
    assert isinstance(data2["context_tickets"], list)
