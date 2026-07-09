from resume_parser import extract_resume_text

resume_path = r"D:\CareerAnalyzer\sample_resumes\AI_Resume.pdf"

text = extract_resume_text(resume_path)

print("Resume Text")
print("-" * 40)
print(text)





import os

folder = r"D:\CareerAnalyzer\sample_resumes"

print("Folder exists:", os.path.exists(folder))
print("Files inside:")

for file in os.listdir(folder):
    print(file)