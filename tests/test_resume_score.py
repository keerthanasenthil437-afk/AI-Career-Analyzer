from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from resume_score import calculate_resume_score

text = extract_resume_text(
    r"D:\CareerAnalyzer\sample_resumes\DataScientist_Resume.pdf"
)

skills = extract_skills(text)

score = calculate_resume_score(text, skills)

print("=" * 40)
print("Resume Score")
print("=" * 40)
print(score, "/100")