import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("models/career_model.pkl", "rb"))

# Load dataset to get feature names
career_data = pd.read_csv("datasets/career_dataset.csv")
feature_names = career_data.drop("Career", axis=1).columns.tolist()


def predict_career(extracted_skills):
    # Create feature vector
    features = []

    for skill in feature_names:
        if skill in extracted_skills:
            features.append(1)
        else:
            features.append(0)

    input_df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(input_df)[0]

    # Get confidence if supported
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = max(model.predict_proba(input_df)[0]) * 100

    return prediction, confidence

