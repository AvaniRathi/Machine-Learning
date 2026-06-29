import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(prompt: str):

    response = model.generate_content(prompt)

    return response.text


def ask_json(prompt: str):

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    return json.loads(text)