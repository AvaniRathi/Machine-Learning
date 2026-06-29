from resume_parser import extract_text
from resume_to_json import parse_resume
import json

resume = extract_text("resume.pdf")

resume_json = parse_resume(resume)

print(json.dumps(resume_json, indent=4))