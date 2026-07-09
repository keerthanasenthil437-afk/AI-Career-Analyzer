import pandas as pd
import re

skills_df = pd.read_csv("datasets/skills.csv")
skill_list = skills_df["Skill"].dropna().tolist()

# Synonyms
skill_alias = {
    "AI": "Artificial Intelligence",
    "ML": "Machine Learning",
    "JS": "JavaScript",
    "Tensor Flow": "TensorFlow",
    "Py Torch": "PyTorch",
    "LLMs": "LLM"
}

def extract_skills(text):

    text_lower = text.lower()

    detected = []

    # Match skills from CSV
    for skill in skill_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            detected.append(skill)

    # Match aliases
    for alias, actual in skill_alias.items():
        pattern = r'\b' + re.escape(alias.lower()) + r'\b'
        if re.search(pattern, text_lower):
            detected.append(actual)

    return sorted(set(detected))