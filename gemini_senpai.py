from config import GEMINI_API_KEY
from google import genai

MODEL = "gemini-2.0-flash"

class GeminiSenpai:
  def __init__(self):
    self.client = genai.Client(api_key=GEMINI_API_KEY)
  
  def send(self, message):
    prompt = self._get_prompt(message)
    
    response = self.client.models.generate_content(
      model=MODEL, contents=prompt
    )

    return response.text

  def _get_prompt(self, message):
    return f"あなたは日本語のプロンプトを受け取ります。以下のメッセージに対して、良い行いなら褒めてください。良くない行いなら、励ましてください。なるべく建設的な内容にしてください。\n「{message}」"

if __name__ == "__main__":
  slack_message = "課題を終わらせた！"
  gemini_senpai = GeminiSenpai()
  response = gemini_senpai.send(slack_message)
  print(response)
