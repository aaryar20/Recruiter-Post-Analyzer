import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None

def match_resume(job_text, resume_text):
    if client is None:
        raise RuntimeError(
            "Gemini API key not configured. Please add GEMINI_API_KEY."
        )

    prompt = f"""
You are an expert technical recruiter.

Compare this resume with this job description.

Return ONLY valid JSON.

Use this structure:

{{
  "match_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "strengths": [],
  "improvements": [],
  "summary": ""
}}

Job Description:

{job_text}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.split("\n",1)[1]
        text = text.rsplit("```",1)[0]

    return json.loads(text)