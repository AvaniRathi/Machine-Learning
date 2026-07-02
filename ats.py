from gemini import ask_json

def ats_score(resume_json, job_description):
    prompt = f"""
You are an ATS system.

Compare the resume with the job description.

Return ONLY valid JSON.

{{
  "score": 0,
  "matched_skills": [],
  "missing_skills": [],
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}}

Resume:
{resume_json}

Job Description:
{job_description}
"""

    return ask_json(prompt)
