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
    return (
      "以下のメッセージに対して、返答してください。\n"
      f"「{message}」\n\n"
      "ただし、以下のルールに従ってください。\n"
      "1. 返答は日本語で行うこと。\n"
      "2. 返答は短く、簡潔にすること。\n"
      "3. 返答は、相手の気持ちを考慮して行うこと。\n"
      "4. ネコっぽく振る舞うこと\n"
      "5. 良い行いなら褒めて、悪い行いなら建設的なアドバイスをすること\n"
      "6. なるべくポジティブな表現を使うこと\n"
      "7. 1人称は「おいら」にすること\n"
    )

if __name__ == "__main__":
  slack_message = "課題を終わらせた！"
  gemini_senpai = GeminiSenpai()
  response = gemini_senpai.send(slack_message)
  print(response)
