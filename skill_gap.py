import pandas as pd

career_data = pd.read_csv("datasets/career_skills.csv")

def analyze_skill_gap(career, user_skills):
    row = career_data[career_data["Career"] == career]

    if row.empty:
        return [], []

    required = row.iloc[0]["Required Skills"].split(",")

    required = [skill.strip() for skill in required]

    user_skills = [skill.strip() for skill in user_skills]

    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return required, missing