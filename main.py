from slack_bolt import App
from config import SLACK_AUTH_TOKEN, SLACK_SIGNING_SECRET

app = App(
  token=SLACK_AUTH_TOKEN,
  signing_secret=SLACK_SIGNING_SECRET
)

@app.event("/reaction_added")
def event(event, say):
  # 特定のメッセージに返信したい
  response = "test"
  say(text=response, thread_ts=event["ts"])
