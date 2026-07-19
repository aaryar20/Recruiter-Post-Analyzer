import streamlit as st
from services.ai_analyzer import analyze_job


def render_ai_analysis(text):

    st.markdown("##AI Job Analysis")

    st.caption(
        "Gemini AI analyzes the job description and extracts the most important hiring information."
    )

    st.markdown("---")

    if st.button(
        "🚀 Analyze Job Description",
        width="stretch"
        ):

        with st.spinner("Gemini is analyzing the job description..."):

            try:

                analysis = analyze_job(text)

                st.markdown("### AI Summary")

                st.info(analysis["summary"])

                left, right = st.columns(2)

                with left:
                    st.markdown("### Experience")
                    st.info(analysis["experience"])

                with right:
                    st.markdown("### Education")
                    st.info(analysis["education"])

                left, right = st.columns(2)

                with left:

                    with st.expander("Responsibilities", expanded=True):

                        for item in analysis["responsibilities"]:
                            st.markdown(f"✅ {item}")

                with right:

                    with st.expander("Soft Skills", expanded=True):

                        for item in analysis["soft_skills"]:
                            st.markdown(f"⭐ {item}")

                st.markdown("---")

                st.markdown("### Resume Keywords")

                keyword_cols = st.columns(3)

                for i, keyword in enumerate(analysis["resume_keywords"]):
                    with keyword_cols[i % 3]:
                        st.success(keyword)

            except Exception as e:
                st.error(f"AI analysis failed: {e}")