from gemini import ask_json


def parse_resume(resume):

    prompt = f"""
You are an ATS Resume Parser.

Return ONLY valid JSON.

Schema:

{{
"name":"",
"email":"",
"phone":"",
"skills":[],
"education":[],
"experience":[],
"projects":[]
}}

Resume:

{resume}
"""

    return ask_json(prompt)