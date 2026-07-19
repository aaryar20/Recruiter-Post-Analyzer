import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter


def render_analytics(df):
    st.markdown("# 📊 Recruiter Analytics Dashboard")

    st.caption(
        "Analyze hiring trends, recruiter activity, skills, and locations extracted from recruiter posts."
        )

    st.markdown("---")
    # -----------------------------
    # Calculate Skills
    # -----------------------------
    all_skills = []

    for skills in df["Skills"]:
        if skills:
            all_skills.extend(
                [
                    s.strip()
                    for s in skills.split(",")
                    if s.strip()
                ]
            )

    skill_counts = Counter(all_skills)
    # -----------------------------
    # Dashboard Cards
    # -----------------------------

    cards = [
        ("📄 Jobs", len(df)),
        ("📧 Recruiters", df["Emails"].nunique()),
        ("📍 Locations", df["Location"].nunique()),
        ("💻 Skills", len(skill_counts)),
    ]

    col1, col2, col3, col4 = st.columns(4)

    for col, (title, value) in zip(
        [col1, col2, col3, col4],
        cards
    ):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <h3>{title}</h3>
                    <h1>{value}</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )
    # -----------------------------
    # Filters
    # -----------------------------
    st.markdown("## 🎛 Filters")

    st.caption(
        "Filter recruiter posts by role, job type, or keyword."
        )

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_role = st.selectbox(
            "Role",
            ["All"] + sorted(df["Role"].unique())
        )

    with filter_col2:
        selected_job_type = st.selectbox(
            "Job Type",
            ["All"] + sorted(df["Job Type"].unique())
        )
    search = st.text_input("🔍 Search by Job Role")

    filtered_df = df.copy()

    if selected_role != "All":
        filtered_df = filtered_df[
            filtered_df["Role"] == selected_role
        ]

    if selected_job_type != "All":
        filtered_df = filtered_df[
            filtered_df["Job Type"] == selected_job_type
        ]

    if search:
        filtered_df = filtered_df[
            filtered_df["Role"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # -----------------------------
    # Table
    # -----------------------------
    st.markdown("## 📋 Extracted Jobs")

    st.caption(
        f"Showing **{len(filtered_df)}** recruiter posts."
    )

    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True
    )

    # -----------------------------
    # Charts
    # -----------------------------
    st.markdown("---")

    st.markdown("## 📈 Hiring Trends")

    st.caption(
        "Visual insights extracted from recruiter posts."
        )

    role_counts = df["Role"].value_counts().reset_index()
    role_counts.columns = ["Role", "Count"]

    job_type_counts = df["Job Type"].value_counts().reset_index()
    job_type_counts.columns = ["Job Type", "Count"]

    location_counts = df["Location"].value_counts().reset_index()
    location_counts.columns = ["Location", "Count"]

    all_skills = []

    for skills in df["Skills"]:
        if skills:
            all_skills.extend(
                [
                    s.strip()
                    for s in skills.split(",")
                    if s.strip()
                ]
            )

    skill_counts = Counter(all_skills)

    skill_df = pd.DataFrame(
        skill_counts.items(),
        columns=["Skill", "Count"]
    ).sort_values(
        by="Count",
        ascending=False
    )

    role_fig = px.bar(
        role_counts,
        x="Role",
        y="Count",
        title="Jobs by Role"
    )

    job_type_fig = px.pie(
        job_type_counts,
        names="Job Type",
        values="Count",
        title="Job Type Distribution"
    )

    location_fig = px.bar(
        location_counts,
        x="Location",
        y="Count",
        title="Jobs by Location"
    )

    skill_fig = px.bar(
        skill_df,
        x="Skill",
        y="Count",
        title="Top Requested Skills"
    )

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.plotly_chart(
                role_fig,
                width="stretch"
            )

    with col2:
        with st.container(border=True):
            st.plotly_chart(
                job_type_fig,
                width="stretch"
            )

    with col3:
        with st.container(border=True):
            st.plotly_chart(
                location_fig,
                width="stretch"
            )

    with col4:
        with st.container(border=True):
            st.plotly_chart(
                skill_fig,
                width="stretch"
            )
    # -----------------------------
    # Dashboard Insights
    # -----------------------------
    st.markdown("---")

    st.markdown("## 💡 Dashboard Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        if not role_counts.empty:
            st.success(
                f"🔥 Most Requested Role\n\n**{role_counts.iloc[0]['Role']}**"
            )

    with col2:
        if not location_counts.empty:
            st.info(
                f"📍 Top Hiring Location\n\n**{location_counts.iloc[0]['Location']}**"
            )

    with col3:
        if not skill_df.empty:
            st.warning(
                f"💻 Top Skill\n\n**{skill_df.iloc[0]['Skill']}**"
            )
    # -----------------------------
    # Download
    # -----------------------------
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.markdown("---")

    st.markdown("## 📥 Export Results")

    st.download_button(
        "📄 Download CSV Report",
        csv,
        "recruiters.csv",
        "text/csv",
        width="stretch"
        )
    #Recruitment Health Score
    score = min(
        100,
        len(df)*5 +
        len(skill_counts)*2
    )

    st.metric(
        "🏆 Recruitment Score",
        f"{score}/100"
    )