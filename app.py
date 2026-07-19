import streamlit as st
import pandas as pd

from services.parser import analyze_posts
from services.file_reader import read_file

from components.sidebar import render_sidebar
from components.analytics import render_analytics
from components.ai_section import render_ai_analysis
from components.matcher_section import render_matcher


def load_css():
    with open("styles/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )



# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Recruiter Post Analyzer",
    page_icon="📄",
    layout="wide"
)
load_css()
render_sidebar()

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div style="
background:linear-gradient(135deg,#2563eb,#1d4ed8);
padding:35px;
border-radius:20px;
color:white;
margin-bottom:25px;
">

<h1 style="margin-bottom:8px;">
🚀 Recruiter Post Analyzer
</h1>

<p style="font-size:18px;">
Analyze recruiter posts, extract hiring insights,
evaluate job descriptions with Gemini AI,
and compare resumes with job requirements.
</p>

</div>
""", unsafe_allow_html=True)
# Upload Section
with st.container(border=True):

    st.subheader("📂 Upload Documents")

    uploaded_file = st.file_uploader(
        "Recruiter Posts",
        type=["txt", "pdf"]
    )

    resume_file = st.file_uploader(
        "Resume (Optional)",
        type=["txt", "pdf"]
    )

# Read resume text
resume_text = ""
if resume_file:
    resume_text = read_file(resume_file)

# -----------------------------
# Tabs
# -----------------------------
analytics_tab, ai_tab, matcher_tab = st.tabs(
    [
        "📊 Recruiter Analytics",
        "🤖 AI Job Analysis",
        "🎯 Resume Matcher"
    ]
)

# -----------------------------
# Continue with Job Analysis
# -----------------------------
if uploaded_file:

    text = read_file(uploaded_file)


    jobs = analyze_posts(text)
    # -----------------------------
    # DataFrame
    # -----------------------------
    df = pd.DataFrame([
        {
            "Role": job.role,
            "Job Type": job.job_type,
            "Location": job.location,
            "Emails": ", ".join(job.emails),
            "Skills": ", ".join(job.skills),
        }
        for job in jobs
    ])

    with analytics_tab:
        render_analytics(df)

    with ai_tab:
        render_ai_analysis(text)

    with matcher_tab:
        render_matcher(text, resume_text)
