from config import GEMINI_API_KEY

from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)

model = "gemini-2.0-flash"
slack_message = "課題を終わらせた！"

def get_prompt(message):
  return f"あなたは日本語のプロンプトを受け取ります。{message}に対して、褒めてください。なるべく自己肯定感を高めて、次も頑張ろうと思えるような内容にしてください。"

response = client.models.generate_content(
  model=model, contents=get_prompt(slack_message)
)

print(response.text)
