import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

def analyze_job(text):

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