
import streamlit as st
import json

from resume_parser import extract_text
from resume_to_json import parse_resume
from ats import ats_score
from interview import generate_questions, evaluate_answer

st.set_page_config(page_title="AI Interview Assistant")

st.title("🤖 AI Interview Assistant")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job = st.text_area("Paste Job Description")

if resume_file and job:

    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())

    resume = extract_text("temp_resume.pdf")

    resume_json = parse_resume(resume)

    st.subheader("Resume JSON")
    st.json(resume_json)

    result = ats_score(resume_json, job)

    st.subheader("ATS Score")

    st.metric("Score", f"{result['score']}%")

    st.write("### Matched Skills")
    st.write(result["matched_skills"])

    st.write("### Missing Skills")
    st.write(result["missing_skills"])

    if st.button("Generate Interview Questions"):

        questions = generate_questions(resume_json, job)

        st.session_state.questions = questions["questions"]


if "questions" in st.session_state:

    st.header("Interview")

    for i, q in enumerate(st.session_state.questions):

        st.write(f"### Question {i+1}")

        st.write(q)

        ans = st.text_area(
            f"Answer {i}",
            key=f"ans{i}"
        )

        if st.button(
            f"Evaluate {i}",
            key=f"btn{i}"
        ):

            evaluation = evaluate_answer(q, ans)

            st.success(
                f"Score : {evaluation['score']}/10"
            )

            st.write("Feedback")

            st.write(evaluation["feedback"])

            st.write("Ideal Answer")

            st.write(evaluation["ideal_answer"])
