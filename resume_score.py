def calculate_resume_score(text, skills):

    text_lower = text.lower()

    # --------------------------------
    # 1. Skills Score - 25
    # --------------------------------

    skill_score = min(len(skills) * 1.5, 25)

    # --------------------------------
    # 2. Projects Score - 20
    # --------------------------------

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented"
    ]

    project_score = 20 if any(
        word in text_lower for word in project_keywords
    ) else 0

    # --------------------------------
    # 3. Education Score - 15
    # --------------------------------

    education_keywords = [
        "b.tech",
        "b.e",
        "b.e.",
        "bachelor",
        "master",
        "m.tech",
        "degree",
        "university",
        "college",
        "education"
    ]

    education_score = 15 if any(
        word in text_lower for word in education_keywords
    ) else 0

    # --------------------------------
    # 4. Contact Information - 10
    # --------------------------------

    contact_score = 0

    if "@" in text:
        contact_score += 5

    if any(char.isdigit() for char in text):
        contact_score += 5

    # --------------------------------
    # 5. Certifications - 10
    # --------------------------------

    certification_keywords = [
        "certificate",
        "certification",
        "certified",
        "coursera",
        "udemy",
        "nptel",
        "aws certification",
        "google certification"
    ]

    certification_score = 10 if any(
        word in text_lower
        for word in certification_keywords
    ) else 0

    # --------------------------------
    # 6. Experience / Internship - 10
    # --------------------------------

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "work experience",
        "professional experience"
    ]

    experience_score = 10 if any(
        word in text_lower
        for word in experience_keywords
    ) else 0

    # --------------------------------
    # 7. Resume Structure - 10
    # --------------------------------

    structure_keywords = [
        "summary",
        "skills",
        "education",
        "projects"
    ]

    sections_found = sum(
        1 for section in structure_keywords
        if section in text_lower
    )

    structure_score = min(
        sections_found * 2.5,
        10
    )

    # --------------------------------
    # Total Score
    # --------------------------------

    total_score = (
        skill_score
        + project_score
        + education_score
        + contact_score
        + certification_score
        + experience_score
        + structure_score
    )

    return round(min(total_score, 100))