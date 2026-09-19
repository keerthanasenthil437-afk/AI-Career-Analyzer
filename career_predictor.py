import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("models/career_model.pkl", "rb"))

# Load dataset to get feature names
career_data = pd.read_csv("datasets/career_dataset.csv")
feature_names = career_data.drop("Career", axis=1).columns.tolist()


# -------------------------------------------------
# Career-specific skill weights
# -------------------------------------------------

career_weights = {

    "AI Engineer": {
        "Artificial Intelligence": 3,
        "LLM": 3,
        "GPT": 3,
        "Claude": 2,
        "Gemini": 2,
        "LangChain": 3,
        "LangGraph": 3,
        "RAG": 3,
        "Prompt Engineering": 2,
        "Pinecone": 2,
        "Computer Vision": 2,
        "NLP": 2,
        "Deep Learning": 2,
        "TensorFlow": 2,
        "PyTorch": 2
    },

    "Data Scientist": {
        "Pandas": 3,
        "NumPy": 3,
        "SQL": 3,
        "Scikit-learn": 3,
        "Machine Learning": 2,
        "Matplotlib": 2,
        "Seaborn": 2,
        "Data Analysis": 3,
        "Data Visualization": 3,
        "XGBoost": 3,
        "A/B Testing": 3,
        "Bayesian": 3,
        "Causal Inference": 3,
        "Excel": 1,
        "Power BI": 1
    },

    "ML Engineer": {
        "Machine Learning": 3,
        "Deep Learning": 3,
        "TensorFlow": 3,
        "PyTorch": 3,
        "Scikit-learn": 2,
        "Docker": 3,
        "Kubernetes": 3,
        "Linux": 2,
        "Git": 2,
        "AWS": 2,
        "MLflow": 3,
        "Airflow": 2,
        "Feast": 2
    },

    "Software Engineer": {
        "Python": 2,
        "Java": 3,
        "C": 3,
        "C++": 3,
        "SQL": 2,
        "Git": 2,
        "GitHub": 2,
        "Linux": 2
    },

    "Full Stack Developer": {
        "HTML": 2,
        "CSS": 2,
        "JavaScript": 3,
        "React": 3,
        "NodeJS": 3,
        "MongoDB": 2,
        "MySQL": 2,
        "Git": 2,
        "GitHub": 2,
        "Bootstrap": 2
    },

    "Frontend Developer": {
        "HTML": 3,
        "CSS": 3,
        "JavaScript": 3,
        "React": 3,
        "Bootstrap": 2,
        "Git": 1
    },

    "Backend Developer": {
        "Python": 2,
        "SQL": 3,
        "NodeJS": 3,
        "Flask": 3,
        "Django": 3,
        "FastAPI": 3,
        "MongoDB": 2,
        "MySQL": 2,
        "Git": 2
    },

    "Web Developer": {
        "HTML": 3,
        "CSS": 3,
        "JavaScript": 3,
        "PHP": 3,
        "Bootstrap": 2,
        "MySQL": 2,
        "Git": 1
    },

    "Cloud Engineer": {
        "AWS": 3,
        "Azure": 3,
        "Docker": 3,
        "Kubernetes": 3,
        "Linux": 3,
        "Git": 2,
        "Python": 1
    },

    "Data Analyst": {
        "SQL": 3,
        "Excel": 3,
        "Power BI": 3,
        "Python": 2,
        "Pandas": 2,
        "Data Analysis": 3,
        "Data Visualization": 3,
        "Matplotlib": 2
    }
}

def predict_career(extracted_skills):

    extracted_skills = set(extracted_skills)

    # Calculate score for every career
    scores = {}

    for career, weights in career_weights.items():

        score = 0

        for skill, weight in weights.items():

            if skill in extracted_skills:
                score += weight

        scores[career] = score

    # Sort careers from highest score to lowest
    ranked_careers = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Get top 3 careers
    top_careers = ranked_careers[:3]

    # Calculate confidence for each career
    recommendations = []

    for career, score in top_careers:

        total_possible = sum(
            career_weights[career].values()
        )

        if total_possible > 0:
            confidence = (score / total_possible) * 100
        else:
            confidence = 0

        confidence = min(confidence, 100)

        recommendations.append(
            (career, confidence)
        )

    # Best career
    prediction = recommendations[0][0]
    confidence = recommendations[0][1]

    return prediction, confidence, recommendations