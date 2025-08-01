#!/usr/bin/env python3
"""
FreshDesk Integration for OpsAI
Handles ticket processing from FreshDesk API for AI operations.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# src/integrations/freshdesk.py

import os
import requests
from src.api.main import classify, resolve

FRESHDESK_DOMAIN = os.getenv("FRESHDESK_DOMAIN")  # e.g. "yourcompany.freshdesk.com"
FRESHDESK_API_KEY = os.getenv("FRESHDESK_API_KEY")


def process_ticket(ticket_id: int):
    # fetch ticket
    url = f"https://{FRESHDESK_DOMAIN}/api/v2/tickets/{ticket_id}"
    resp = requests.get(url, auth=(FRESHDESK_API_KEY, "X"))
    data = resp.json()
    text = data["subject"] + " " + data["description"]

    # classify & resolve
    cls = classify.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))
    res = resolve.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))

    # add private note
    note_url = f"{url}/notes"
    note = {
        "body": f"*OpsAI Tags:* {cls.tags}\n*Suggestion:* {res.suggestion}",
        "private": True
    }
    requests.post(note_url, json=note, auth=(FRESHDESK_API_KEY, "X"))


if __name__ == "__main__":
    # example: process ticket #123
    process_ticket(123)
