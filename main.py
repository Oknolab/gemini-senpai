from slack_bolt import App
from config import SLACK_AUTH_TOKEN, SLACK_SIGNING_SECRET, SLACK_APP_TOKEN
from slack_bolt.adapter.socket_mode import SocketModeHandler
from gemini_senpai import GeminiSenpai

app = App(
  token=SLACK_AUTH_TOKEN,
)

gemini_senpai = GeminiSenpai()

replied_messages = set()

@app.event("reaction_added")
def handle_reaction(event, client, logger):
  reaction = event["reaction"]
  channel = event["item"]["channel"]
  timestamp = event["item"]["ts"]

  if reaction != "gemini-homehome":
    return

  result = client.conversations_history(
    channel=channel,
    latest=timestamp,
    inclusive=True,
    limit=1
  )

  messages = result.get("messages", [])
  if not messages:
    return
  
  message_timestamp = messages[0]["ts"]
  if message_timestamp in replied_messages:
    return
  replied_messages.add(message_timestamp)
  
  original_message = messages[0]["text"]

  gemini_response = gemini_senpai.send(original_message)

  client.chat_postMessage(
    channel=channel,
    thread_ts=timestamp,
    text=gemini_response,
  )
  
if __name__ == "__main__":
  SocketModeHandler(app, SLACK_APP_TOKEN).start()
