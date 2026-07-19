import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def match_resume(job_text, resume_text):

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