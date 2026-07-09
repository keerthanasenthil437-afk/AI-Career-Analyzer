from readiness import calculate_readiness

skills = [
    "Python",
    "Machine Learning",
    "SQL"
]

career = "ML Engineer"

score = calculate_readiness(career, skills)

print("Career Readiness:", score, "%")