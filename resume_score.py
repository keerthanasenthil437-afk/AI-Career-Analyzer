def calculate_resume_score(text, skills):

    score = 0

    # Skill Score (40)
    score += min(len(skills) * 2, 40)

    # Projects
    if "project" in text.lower():
        score += 20

    # Education
    education_keywords = [
        "b.tech",
        "b.e",
        "bachelor",
        "master",
        "m.tech",
        "degree"
    ]

    if any(word in text.lower() for word in education_keywords):
        score += 20

    # Certifications
    certification_keywords = [
        "certificate",
        "certification",
        "coursera",
        "udemy",
        "aws"
    ]

    if any(word in text.lower() for word in certification_keywords):
        score += 20

    return min(score, 100)