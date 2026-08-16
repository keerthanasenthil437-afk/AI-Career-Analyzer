import pandas as pd
import random

random.seed(42)

# ----------------------------
# Skills (55 features)
# ----------------------------

skills = [
    # Programming
    "Python", "Java", "C", "C++", "SQL",

    # Web Development
    "HTML", "CSS", "JavaScript", "React", "NodeJS",
    "PHP", "Bootstrap",

    # Machine Learning / AI
    "Machine Learning", "Deep Learning",
    "Artificial Intelligence", "TensorFlow", "PyTorch",
    "Scikit-learn", "Pandas", "NumPy",
    "Matplotlib", "Seaborn",

    # Development / DevOps
    "Git", "GitHub", "Docker", "Kubernetes",
    "AWS", "Azure", "Linux",

    # Backend
    "Flask", "Django", "FastAPI",

    # Databases
    "MongoDB", "MySQL",

    # Data
    "Power BI", "Excel",
    "Data Analysis", "Data Visualization",

    # AI Specializations
    "Computer Vision", "NLP",

    # Modern Generative AI
    "LLM", "GPT", "Claude", "Gemini",
    "Llama", "Mistral",
    "LangChain", "LangGraph",
    "RAG", "Pinecone",
    "Chroma", "Weaviate",
    "CrewAI", "Prompt Engineering"
   
    # Data Science / MLOps
    "XGBoost",
    "A/B Testing",
    "Bayesian",
    "Causal Inference",
    "MLflow",
    "Airflow",
    "Feast"
]


# ----------------------------
# Career Profiles
# ----------------------------

career_profiles = {

    "AI Engineer": [
        "Python", "SQL",
        "Machine Learning", "Deep Learning",
        "Artificial Intelligence",
        "TensorFlow", "PyTorch",
        "Scikit-learn", "Pandas", "NumPy",
        "LLM", "GPT", "Claude", "Gemini",
        "Llama", "Mistral",
        "LangChain", "LangGraph", "RAG",
        "Pinecone", "Chroma", "Weaviate",
        "CrewAI", "Prompt Engineering",
        "Git", "Docker", "Linux",
        "Computer Vision", "NLP"
    ],

    "Data Scientist": [
    "Python",
    "SQL",
    "Machine Learning",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "Excel",
    "Power BI",
    "Data Analysis",
    "Data Visualization",
    "XGBoost",
    "A/B Testing",
    "Bayesian",
    "Causal Inference"
   ],
    "ML Engineer": [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Docker",
    "Kubernetes",
    "Linux",
    "Git",
    "AWS",
    "MLflow",
    "Airflow",
    "Feast"
],
    "Software Engineer": [
        "Python", "Java", "C", "C++",
        "SQL",
        "Git", "GitHub", "Linux"
    ],

    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "NodeJS",
        "MongoDB", "MySQL",
        "Git", "GitHub", "Bootstrap"
    ],

    "Frontend Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Bootstrap", "Git"
    ],

    "Backend Developer": [
        "Python", "SQL",
        "NodeJS",
        "Flask", "Django", "FastAPI",
        "MongoDB", "MySQL",
        "Git"
    ],

    "Web Developer": [
        "HTML", "CSS", "JavaScript",
        "PHP", "Bootstrap",
        "MySQL", "Git"
    ],

    "Cloud Engineer": [
        "Python",
        "AWS", "Azure",
        "Docker", "Kubernetes",
        "Linux", "Git"
    ],

    "Data Analyst": [
        "SQL", "Excel",
        "Power BI",
        "Python", "Pandas",
        "Data Analysis",
        "Data Visualization",
        "Matplotlib"
    ]
}


# ----------------------------
# Generate Dataset
# ----------------------------

rows = []

for i in range(1000):

    career = random.choice(list(career_profiles.keys()))

    required = set(career_profiles[career])

    row = {}

    for skill in skills:

        if skill in required:

            # Required skills have high probability
            row[skill] = random.choices(
                [1, 0],
                weights=[95, 5]
            )[0]

        else:

            # Non-required skills have very low probability
            row[skill] = random.choices(
                [1, 0],
                weights=[3, 97]
            )[0]

    row["Career"] = career

    rows.append(row)


# ----------------------------
# Create DataFrame
# ----------------------------

df = pd.DataFrame(rows)


# ----------------------------
# Save Dataset
# ----------------------------

df.to_csv(
    "datasets/career_dataset.csv",
    index=False
)


print("Dataset Created Successfully!")

print("Number of rows:", len(df))

print("Number of features:", len(skills))

print("Shape:", df.shape)

print("\nCareer Distribution:")

print(df["Career"].value_counts())

print("\nFirst 5 rows:")

print(df.head())