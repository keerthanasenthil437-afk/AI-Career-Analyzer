def get_improvement_suggestions(
    text,
    skills,
    missing_skills,
    resume_score
):

    suggestions = []

    text_lower = text.lower()
    skills_lower = [skill.lower() for skill in skills]

    # Missing skills
    if missing_skills:

        suggestions.append(
            "⚠️ Consider learning: "
            + ", ".join(missing_skills)
            + "."
        )

    # Experience
    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "work experience"
    ]

    if not any(word in text_lower for word in experience_keywords):

        suggestions.append(
            "⚠️ Add internship or practical work experience "
            "if available."
        )

    # Certifications
    certification_keywords = [
        "certification",
        "certificate",
        "coursera",
        "udemy",
        "nptel"
    ]

    if not any(
        word in text_lower
        for word in certification_keywords
    ):

        suggestions.append(
            "⚠️ Consider adding relevant certifications "
            "to strengthen your resume."
        )

    # Projects
    if "project" not in text_lower:

        suggestions.append(
            "⚠️ Add academic or personal projects "
            "with measurable outcomes."
        )

    # Git/GitHub
    if "git" not in skills_lower:

        suggestions.append(
            "⚠️ Add Git/GitHub experience if you have used it."
        )

    # Resume score
    if resume_score >= 80:

        suggestions.append(
            "✅ Your resume has a strong overall structure."
        )

    elif resume_score >= 60:

        suggestions.append(
            "💡 Your resume is good, but there is room "
            "for improvement."
        )

    else:

        suggestions.append(
            "⚠️ Your resume needs improvement in several areas."
        )

    return suggestions