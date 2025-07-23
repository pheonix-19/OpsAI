# src/integrations/slack_bot.py

import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ─── Load .env ─────────────────────────────────────────────────────────
load_dotenv()  # reads .env in the project root

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
MENTION_TRIGGER = f"<@{os.getenv('YOUR_BOT_USER_ID')}>"  # use the env var

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mention(body, say):
    from src.api.main import classify, resolve  # local import to avoid cycles

    text = body["event"]["text"].replace(MENTION_TRIGGER, "").strip()
    cls = classify.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))
    say(f"*Tags:* {', '.join(cls.tags)}\n*Teams:* {', '.join(cls.teams)}")

    res = resolve.__wrapped__(type("Q", (), {"text": text, "top_k": 3}))
    say(f"*Suggestion:* {res.suggestion}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
