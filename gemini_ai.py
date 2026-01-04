import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-flash-latest"

def clean_ai_response(text: str) -> str:
    return re.sub(r"\*+", "", text).strip()

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if not response or not response.text:
            return "I did not receive a response from Gemini."

        return clean_ai_response(response.text)

    except Exception as e:
        return f"AI error: {e}"


# standalone test
# if __name__ == "__main__":
#     print(f"[Gemini] Model: {MODEL_NAME}")
#     print(ask_gemini("What is Python?"))
