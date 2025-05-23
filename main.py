from slack_bolt import App
from config import SLACK_AUTH_TOKEN, SLACK_SIGNING_SECRET, SLACK_APP_TOKEN
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(
  token=SLACK_AUTH_TOKEN,
  # signing_secret=SLACK_SIGNING_SECRET
)

# @app.event("/reaction_added")
# def reaction_added(event, say):
#   # 特定のメッセージに返信したい
#   response = "test"
#   say(text=response, thread_ts=event["ts"])

@app.message("こんにちは")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"こんにちは、<@{message['user']}> さん！")

if __name__ == "__main__":
    # アプリを起動して、ソケットモードで Slack に接続します
    SocketModeHandler(app, SLACK_APP_TOKEN).start()

