import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None

def analyze_job(text):
    if client is None:
        raise RuntimeError(
            "Gemini API key not configured. Please add GEMINI_API_KEY."
        )

    prompt = f"""
You are an expert technical recruiter.

Analyze the following job post.

Return ONLY valid JSON.

Use this exact structure:

{{
  "summary": "",
  "experience": "",
  "education": "",
  "responsibilities": [],
  "soft_skills": [],
  "resume_keywords": []
}}

Job Post:

{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    response_text = response.text.strip()

    if response_text.startswith("```"):
        response_text = response_text.split("\n", 1)[1]
        response_text = response_text.rsplit("```", 1)[0]

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        return {
            "summary": response_text,
            "experience": "Not available",
            "education": "Not available",
            "responsibilities": [],
            "soft_skills": [],
            "resume_keywords": [],
            }