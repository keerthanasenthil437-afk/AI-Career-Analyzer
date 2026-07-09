from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from career_predictor import predict_career

resume_path = r"D:\CareerAnalyzer\sample_resumes\AI_Resume.pdf"

# Extract text
text = extract_resume_text(resume_path)

# Extract skills
skills = extract_skills(text)

print("=" * 50)
print("Detected Skills")
print("=" * 50)

for skill in skills:
    print("✔", skill)

print("\nTotal Skills:", len(skills))

# Predict career
career, confidence = predict_career(skills)

print("\n" + "=" * 50)
print("Predicted Career")
print("=" * 50)
print("Career:", career)

if confidence is not None:
    print(f"Confidence: {confidence:.2f}%")