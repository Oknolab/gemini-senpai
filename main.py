from slack_bolt import App
from config import SLACK_AUTH_TOKEN, SLACK_SIGNING_SECRET, SLACK_APP_TOKEN
from slack_bolt.adapter.socket_mode import SocketModeHandler
from gemini_senpai import GeminiSenpai

app = App(
  token=SLACK_AUTH_TOKEN,
)

gemini_senpai = GeminiSenpai()

@app.event("reaction_added")
def handle_reaction(event, client, logger):
  reaction = event["reaction"]
  channel = event["item"]["channel"]
  timestamp = event["item"]["ts"]

  logger.info(f"Reaction '{reaction}' added to message {timestamp} in channel {channel}")

  result = client.conversations_history(
      channel=channel,
      latest=timestamp,
      inclusive=True,
      limit=1
  )

  messages = result.get("messages", [])
  if not messages:
      logger.warn("Message not found.")
      return
  
  original_message = messages[0]["text"]
  logger.info(f"Original message: {original_message}")

  gemini_response = gemini_senpai.send(original_message)

  if reaction == "gemini-homehome":
    client.chat_postMessage(
        channel=channel,
        thread_ts=timestamp,  # スレッドとして返信
        text=gemini_response,
    )

if __name__ == "__main__":
  # アプリを起動して、ソケットモードで Slack に接続します
  SocketModeHandler(app, SLACK_APP_TOKEN).start()
