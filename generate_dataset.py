import pandas as pd
import random

random.seed(42)

# ----------------------------
# Skills (40 features)
# ----------------------------
skills = [
    "Python", "Java", "C", "C++", "SQL",
    "HTML", "CSS", "JavaScript", "React", "NodeJS",
    "PHP", "Bootstrap", "Machine Learning", "Deep Learning",
    "Artificial Intelligence", "TensorFlow", "PyTorch",
    "Scikit-learn", "Pandas", "NumPy",
    "Matplotlib", "Seaborn", "Git", "GitHub",
    "Docker", "Kubernetes", "AWS", "Azure",
    "Linux", "Flask", "Django", "FastAPI",
    "MongoDB", "MySQL", "Power BI", "Excel",
    "Data Analysis", "Data Visualization",
    "Computer Vision", "NLP"
]

# ----------------------------
# Career Profiles
# ----------------------------

career_profiles = {

    "AI Engineer":[
        "Python","SQL","Machine Learning","Deep Learning",
        "Artificial Intelligence","TensorFlow","PyTorch",
        "Scikit-learn","Pandas","NumPy",
        "Git","Docker","Linux","Computer Vision","NLP"
    ],

    "Data Scientist":[
        "Python","SQL","Machine Learning","Pandas","NumPy",
        "Matplotlib","Seaborn","Scikit-learn",
        "Excel","Power BI","Data Analysis",
        "Data Visualization","Git"
    ],

    "ML Engineer":[
        "Python","Machine Learning","Deep Learning",
        "TensorFlow","PyTorch","Docker",
        "Linux","Git","AWS","Scikit-learn"
    ],

    "Software Engineer":[
        "Python","Java","C","C++",
        "SQL","Git","GitHub","Linux"
    ],

    "Full Stack Developer":[
        "HTML","CSS","JavaScript","React",
        "NodeJS","MongoDB","MySQL",
        "Git","GitHub","Bootstrap"
    ],

    "Frontend Developer":[
        "HTML","CSS","JavaScript",
        "React","Bootstrap","Git"
    ],

    "Backend Developer":[
        "Python","SQL","NodeJS","Flask",
        "Django","FastAPI","MongoDB",
        "MySQL","Git"
    ],

    "Web Developer":[
        "HTML","CSS","JavaScript",
        "PHP","Bootstrap","MySQL","Git"
    ],

    "Cloud Engineer":[
        "Python","AWS","Azure",
        "Docker","Kubernetes",
        "Linux","Git"
    ],

    "Data Analyst":[
        "SQL","Excel","Power BI",
        "Python","Pandas","Data Analysis",
        "Data Visualization","Matplotlib"
    ]

}

rows = []

# ----------------------------
# Generate 500 rows
# ----------------------------

for i in range(500):

    career = random.choice(list(career_profiles.keys()))

    required = career_profiles[career]

    row = {}

    for skill in skills:

        if skill in required:
            row[skill] = random.choices([1,0], weights=[90,10])[0]
        else:
            row[skill] = random.choices([1,0], weights=[15,85])[0]

    row["Career"] = career

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("datasets/career_dataset.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())
print("Shape:", df.shape)

