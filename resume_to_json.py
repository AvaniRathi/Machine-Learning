
from gemini import ask_json

def parse_resume(resume):

    prompt = f"""
You are an ATS parser.

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
