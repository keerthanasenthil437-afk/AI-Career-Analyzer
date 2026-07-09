import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from career_predictor import predict_career
from skill_gap import analyze_skill_gap
from roadmap import get_roadmap
from recommendation import get_projects
from certifications import get_certifications
from resume_score import calculate_resume_score
from readiness import calculate_readiness

st.set_page_config(
    page_title="AI Career Roadmap & Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("🎯 AI Career Analyzer")

st.sidebar.markdown("---")

st.sidebar.write("👩‍💻 **Developed By**")
st.sidebar.success("Keerthana Senthilkumar")

st.sidebar.write("🎓 B.E Computer Science")

st.sidebar.write("🤖 AI & Machine Learning Project")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Upload a resume to receive:
    - Career Prediction
    - Resume Score
    - Career Readiness
    - Skill Gap Analysis
    - Learning Roadmap
    - Project Suggestions
    - Certifications
    """
)
    

st.title("🎯 AI Career Roadmap & Skill Gap Analyzer")

st.write(
    "Upload your resume and get career prediction, skill analysis, "
    "learning roadmap, projects and certifications."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    # Extract Resume Text
    text = extract_resume_text(uploaded_file)

    st.subheader("📄 Resume Preview")
    st.text_area(
        "Extracted Text",
        text[:1500],
        height=250
    )

    # Extract Skills
    skills = extract_skills(text)

    st.subheader("🧠 Detected Skills")
    
    if skills:

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].success(skill)

    else:

        st.warning("No skills detected.")

    st.info(f"Total Skills Detected : {len(skills)}")

    # Career Prediction
    career, confidence = predict_career(skills)
    st.subheader("🎯 Career Prediction")
    st.success(f"Recommended Career : {career}")

    if confidence is not None:

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(confidence/100)    
    # Calculate Resume Score
    resume_score = calculate_resume_score(text, skills)

    # Calculate Career Readiness
    readiness = calculate_readiness(career, skills)

    col1, col2 = st.columns(2)
    with col1:

        st.subheader("⭐ Resume Score")

        st.metric(
            "Score",
            f"{resume_score}/100"
        )

        st.progress(resume_score/100)

    with col2:

        st.subheader("📈 Career Readiness")

        st.metric(
            "Readiness",
            f"{readiness}%"
        )

        st.progress(readiness/100)
    # Skill Gap Analysis
    required, missing = analyze_skill_gap(career, skills)

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