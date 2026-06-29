import re


def clean(text):

    return text.lower().strip()


def keyword_match(resume, jd):

    resume_words = set(re.findall(r"\w+", clean(resume)))

    jd_words = set(re.findall(r"\w+", clean(jd)))

    matched = resume_words.intersection(jd_words)

    score = len(matched) / len(jd_words) * 100

    return round(score, 2), matched