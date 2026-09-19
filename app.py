import streamlit as st
from pathlib import Path
import pandas as pd

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from career_predictor import predict_career
from skill_gap import analyze_skill_gap
from roadmap import get_roadmap
from recommendation import get_projects
from certifications import get_certifications
from resume_score import calculate_resume_score
from readiness import calculate_readiness
from improvements import get_improvement_suggestions


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="CareerLens AI",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# Load Custom CSS
# -----------------------------

css_path = Path("style.css")

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -----------------------------
# Top Navigation
# -----------------------------

st.html("""
<style>

.career-nav {
    width: 100%;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px 25px;
    margin-bottom: 35px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    box-shadow: 0 4px 15px rgba(15, 23, 42, 0.06);
}

.career-brand {
    font-size: 21px;
    font-weight: 800;
    color: #1f2937;
    white-space: nowrap;
}

.career-links {
    display: flex;
    align-items: center;
    gap: 28px;
}

.career-links a {
    text-decoration: none;
    color: #4b5563;
    font-size: 15px;
    font-weight: 600;
    transition: 0.2s;
}

.career-links a:hover {
    color: #4f46e5;
}

.career-links .active {
    color: #4f46e5;
}

</style>

<div class="career-nav">

    <div class="career-brand">
        🎯 CareerLens AI
    </div>

    <div class="career-links">

        <a class="active" href="#top">
            Home
        </a>

        <a href="#analyze-your-resume">
            Analyze Resume
        </a>

        <a href="#learning-roadmap">
            Roadmap
        </a>

        <a href="#recommended-projects">
            Projects
        </a>

        <a href="#recommended-certifications">
            Certifications
        </a>

    </div>

</div>
""")
#-----------------------------
# Feature Cards
# -----------------------------

feature_col1, feature_col2, feature_col3, feature_col4 = st.columns(4)

with feature_col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Career Prediction</h3>
            <p>Find your best-fit career based on your skills.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⭐</div>
            <h3>Resume Score</h3>
            <p>Evaluate the strength of your resume.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>Skill Gap</h3>
            <p>Discover the skills you need to improve.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <h3>Career Roadmap</h3>
            <p>Get a personalized path to your target career.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
# -----------------------------
# Resume Upload Section
# -----------------------------

# -----------------------------
# Resume Upload Section
# -----------------------------

st.subheader("📄 Analyze Your Resume")

st.write(
    "Upload your resume to unlock your personalized career insights."
)

uploaded_file = st.file_uploader(
    "Drop your resume here or browse your files",
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX"
)

if uploaded_file is not None:
    st.success(
        f"✅ Resume uploaded successfully: {uploaded_file.name}"
    )

    # Extract Resume Text
    text = extract_resume_text(uploaded_file)

    st.subheader("📄 Resume Preview")
    with st.expander("View Extracted Resume Text", expanded=False):
        st.text_area(
            "Extracted Text",
            text[:1500],
            height=250,
            label_visibility="collapsed"
        )

    # Extract Skills
    skills = extract_skills(text)

    # -----------------------------
    # Detected Skills
    # -----------------------------

    st.subheader("🧠 Detected Skills")

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            with cols[i % 4]:

                st.markdown(
                    f"""
                    <div style="
                        background: #f5f3ff;
                        border: 1px solid #ddd6fe;
                        border-radius: 10px;
                        padding: 10px;
                        margin-bottom: 10px;
                        text-align: center;
                        font-weight: 600;
                        color: #4f46e5;
                    ">
                        {skill}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:

        st.warning("No skills detected.")

    st.info(f"🧠 Total Skills Detected: {len(skills)}")
    # -----------------------------
    # Career Prediction
    # -----------------------------

    career, confidence, recommendations = predict_career(skills)

    st.subheader("🎯 Career Prediction")

    st.success(f"🎯 Recommended Career: {career}")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )

    with col2:
        st.metric(
            "Career",
            career
        )

    st.progress(confidence / 100)

    # -----------------------------
    # Top Career Recommendations
    # -----------------------------

    st.subheader("🏆 Top Career Recommendations")

    rec_col1, rec_col2, rec_col3 = st.columns(3)

    top_careers = recommendations[:3]
    medals = ["🥇", "🥈", "🥉"]
    rec_cols = [rec_col1, rec_col2, rec_col3]

    for i, (career_name, career_confidence) in enumerate(top_careers):

        with rec_cols[i]:

            st.markdown(f"### {medals[i]}")

            st.markdown(
                f"**{career_name}**"
            )

            st.success(
                f"{career_confidence:.2f}% Match"
            )


    # Calculate Resume Score
    resume_score = calculate_resume_score(text, skills)




    # Calculate Career Readiness
    readiness, matched_count, missing_count = calculate_readiness(
    career,
    skills
)
    # -----------------------------
    # Resume Score & Career Readiness
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("⭐ Resume Score")

            st.metric(
                "Score",
                f"{resume_score}/100"
            )

            st.progress(resume_score / 100)

            st.caption(
                "Overall strength of your resume"
            )


    with col2:

        with st.container(border=True):

            st.subheader("📈 Career Readiness")

            st.metric(
                "Readiness",
                f"{readiness}%"
            )

            st.progress(readiness / 100)

            st.write(
                f"✅ Skills Matched: {matched_count}"
            )

            st.write(
                f"❌ Skills Missing: {missing_count}"
            )

            st.caption(
                f"Your readiness for {career}"
            )


    # -----------------------------
    # Performance Comparison
    # -----------------------------

    st.subheader("📊 Resume Performance")

    chart_data = pd.DataFrame({
        "Metric": ["Resume Score", "Career Readiness"],
        "Percentage": [resume_score, readiness]
    })

    st.bar_chart(
        chart_data.set_index("Metric"),
        height=300
    )




    # Skill Gap Analysis
    required, missing = analyze_skill_gap(career, skills)
    # Resume Improvement Suggestions
    
    suggestions = get_improvement_suggestions(
        text,
        skills,
        missing,
        resume_score
    )

    st.subheader("💡 Resume Improvement Suggestions")

    for suggestion in suggestions:
        st.write(suggestion)

    col1, col2 = st.columns(2)
    with col1:

        st.subheader("📌 Required Skills")

        for skill in required:
            st.success(skill)

    with col2:

        st.subheader("❌ Missing Skills")

        if missing:

            for skill in missing:
                st.error(skill)

        else:

            st.success("No Missing Skills 🎉")
    st.subheader("🎯 Focus Areas")

    if missing:

        st.write(
            "Improve these skills to increase your career readiness:"
        )

        for skill in missing:
            st.warning(f"📚 {skill}")

    else:

        st.success(
            "🎉 You have all the required skills for this career!"
        )

    # Learning Roadmap
    roadmap = get_roadmap(career)

    st.subheader("🗓️ Learning Roadmap")

    for week in roadmap:
        st.write("✅", week)

    # Recommended Projects
    projects = get_projects(career)

    st.subheader("💻 Recommended Projects")

    for project in projects:
        st.write("🚀", project)

    # Certifications
    certs = get_certifications(career)

    st.subheader("🎓 Recommended Certifications")

    for cert in certs:
        st.write("🏅", cert)
        
        
st.markdown("---")

st.caption(
    "AI Career Roadmap & Skill Gap Analyzer | Developed using Python, Machine Learning, NLP & Streamlit"
)