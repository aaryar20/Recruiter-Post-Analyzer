import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055687.png", width=70)

        st.title("Recruiter Post Analyzer")

        st.caption(
            "AI-powered recruiter post analytics built with Gemini."
        )

        st.markdown("---")

        st.markdown("### 📊 Features")

        st.markdown("""
        ✅ Recruiter Post Parser

        🤖 AI Job Analysis

        🎯 Resume Matcher

        📈 Analytics Dashboard

        📥 CSV Export
        """)

        st.markdown("---")

        st.info(
            "Built with Streamlit • Gemini AI • Plotly"
        )

        st.markdown("---")

        st.caption("© 2026 Aarya Rashinker")