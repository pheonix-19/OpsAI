#!/usr/bin/env python3
"""
OpsAI Jira Integration

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module provides Jira integration for automated ticket processing.
"""

import os
from dotenv import load_dotenv
from fastapi import APIRouter, Header, HTTPException
from jira import JIRA
from pydantic import BaseModel

# ─── Load .env ─────────────────────────────────────────────────────────
load_dotenv()  # reads ~/opsai/.env

# ─── Config from environment ────────────────────────────────────────────
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
WEBHOOK_SECRET = os.getenv("JIRA_WEBHOOK_SECRET", "")

if not (JIRA_URL and JIRA_USER and JIRA_API_TOKEN):
    raise RuntimeError("JIRA_URL, JIRA_USER, and JIRA_API_TOKEN must be set in .env")

# ─── Jira client ────────────────────────────────────────────────────────
jira_client = JIRA(
    server=JIRA_URL,
    basic_auth=(JIRA_USER, JIRA_API_TOKEN)
)

router = APIRouter()


class IssuePayload(BaseModel):
    issue: dict
    timestamp: str


@router.post("/jira/webhook")
async def handle_jira_webhook(
    payload: IssuePayload,
    x_jira_webhook_secret: str = Header(None)
):
    # verify secret if configured
    if WEBHOOK_SECRET and x_jira_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(403, "Invalid webhook secret")

    # lazy‑import to avoid circular dependency
    from src.api.main import classify, resolve

    issue = payload.issue
    key = issue["key"]
    fields = issue["fields"]
    summary = fields.get("summary", "")
    desc = fields.get("description", "")
    text = f"{summary}\n{desc}"

    cls = await classify.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))
    res = await resolve.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))

    comment = (
        f"*OpsAI suggestions*\n"
        f"> *Tags:* {', '.join(cls.tags)}\n"
        f"> *Teams:* {', '.join(cls.teams)}\n\n"
        f"*Resolution:* {res.suggestion}"
    )
    jira_client.add_comment(issue=key, body=comment)
    return {"status": "ok"}
