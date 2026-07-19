import streamlit as st
from services.resume_matcher import match_resume

def render_matcher(job_text, resume_text):

    st.markdown("## 🎯 Resume Matcher")

    st.caption(
        "Compare your resume with the selected job description using Gemini AI."
    )

    st.markdown("---")

    if not resume_text:
        st.warning(
            "📄 Upload a resume to compare it with the recruiter post."
            )
        return

    if st.button(
        "🚀 Analyze Resume",
        width="stretch"
    ):

        with st.spinner("🤖 Gemini is evaluating your resume..."):

            try:
                result = match_resume(job_text, resume_text)

                # all your existing code goes here

            except Exception as e:
                st.error(f"Resume analysis failed: {e}")

            score = result["match_score"]

            if score >= 80:
                status = "🟢 Excellent Match"

            elif score >= 60:
                status = "🟡 Good Match"

            else:
                status = "🔴 Needs Improvement"

            st.markdown(
                f"""
                <div class="metric-card">

                <h3>🎯 Resume Match Score</h3>

                <h1>{score}%</h1>

                <p>{status}</p>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.progress(score/100)

            left, right = st.columns(2)

            with left:

                st.markdown("### ✅ Matching Skills")

                if result["matching_skills"]:

                    for skill in result["matching_skills"]:
                        st.success(skill)

                else:
                    st.info("No matching skills found.")

            left, right = st.columns(2)

            with left:

                st.markdown("### ✅ Matching Skills")

                if result["matching_skills"]:
                    for skill in result["matching_skills"]:
                        st.success(skill)
                else:
                    st.info("No matching skills found.")

            with right:

                st.markdown("### ❌ Missing Skills")

                if result["missing_skills"]:
                    for skill in result["missing_skills"]:
                        st.error(skill)
                else:
                    st.success("No missing skills!")
            left, right = st.columns(2)

            with left:

                st.markdown("### 💪 Strengths")

                for item in result["strengths"]:
                    st.markdown(f"✅ {item}")

            with right:

                st.markdown("### 🚀 Improvements")

                for item in result["improvements"]:
                    st.markdown(f"📌 {item}")