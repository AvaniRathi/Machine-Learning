
from gemini import ask_json


def generate_questions(resume_json, job_description):

    prompt = f"""
You are a senior technical interviewer.

Generate 10 interview questions based on the resume and job description.

Return ONLY valid JSON.

{{
    "questions":[]
}}

Resume:
{resume_json}

Job Description:
{job_description}
"""

    return ask_json(prompt)


def evaluate_answer(question, answer):

    prompt = f"""
You are a senior technical interviewer.

Evaluate the candidate's answer.

Return ONLY valid JSON.

{{
    "score":0,
    "feedback":"",
    "ideal_answer":""
}}

Question:
{question}

Candidate Answer:
{answer}
"""

    return ask_json(prompt)
