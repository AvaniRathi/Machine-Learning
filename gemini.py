
import google.generativeai as genai
import json

API_KEY = "AQ.Ab8RN6Ly9_7uEcSpUwPJk67AOOCS6quPVdhsT1Dai-bCaqr_Tg"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(prompt):
    response = model.generate_content(prompt)
    return response.text


def ask_json(prompt):
    response = model.generate_content(prompt)

    text = response.text
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)
