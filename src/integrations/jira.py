# src/integrations/jira.py

import os
from fastapi import APIRouter, Header, HTTPException
from jira import JIRA
from pydantic import BaseModel
import requests

from src.api.main import classify, resolve  # reuse our API logic

router = APIRouter()

# load from env
JIRA_URL      = os.getenv("JIRA_URL")
JIRA_USER     = os.getenv("JIRA_USER")
JIRA_API_TOKEN= os.getenv("JIRA_API_TOKEN")
WEBHOOK_SECRET= os.getenv("JIRA_WEBHOOK_SECRET", "")

jira_client = JIRA(
    server=JIRA_URL,
    basic_auth=(JIRA_USER, JIRA_API_TOKEN)
)

class IssuePayload(BaseModel):
    issue: dict
    timestamp: str

@router.post("/jira/webhook")
async def handle_jira_webhook(
    payload: IssuePayload,
    x_jira_webhook_secret: str = Header(None)
):
    # optional secret verification
    if WEBHOOK_SECRET and x_jira_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(403, "Invalid webhook secret")

    issue = payload.issue
    key   = issue["key"]
    fields= issue["fields"]
    summary = fields["summary"]
    desc    = fields.get("description", "")
    text    = f"{summary}\n{desc}"

    # classify & resolve
    cls = await classify.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))
    res = await resolve.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))

    # post comment
    comment = (
        f"*OpsAI suggestions*\n"
        f"> *Tags:* {', '.join(cls.tags)}\n"
        f"> *Teams:* {', '.join(cls.teams)}\n\n"
        f"*Resolution:* {res.suggestion}"
    )
    jira_client.add_comment(issue=key, body=comment)
    return {"status": "ok"}
