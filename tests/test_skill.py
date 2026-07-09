from resume_parser import extract_resume_text
from skill_extractor import extract_skills

resume_path = r"D:\CareerAnalyzer\sample_resumes\AI_Resume.pdf"

text = extract_resume_text(resume_path)

skills = extract_skills(text)

print("=" * 40)
print("Detected Skills")
print("=" * 40)

for skill in skills:
    print("✔", skill)

print("\nTotal Skills:", len(skills))