from skill_gap import analyze_skill_gap

career = "ML Engineer"

skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

required, missing = analyze_skill_gap(career, skills)

print("Career:", career)

print("\nRequired Skills")
for s in required:
    print("✔", s)

print("\nMissing Skills")
for s in missing:
    print("❌", s)