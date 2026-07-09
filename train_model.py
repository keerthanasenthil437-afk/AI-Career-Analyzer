import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

# ML Algorithms
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("datasets/career_dataset.csv")

# Features and Target
X = df.drop("Career", axis=1)
y = df["Career"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Compare Different Models
# -----------------------------
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": SVC(probability=True, random_state=42)
}

best_model = None
best_accuracy = 0
best_model_name = ""

print("Model Comparison")
print("-" * 30)

for name, model in models.items():
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    print(f"{name}: {accuracy:.2f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# -----------------------------
# Save Best Model
# -----------------------------
pickle.dump(best_model, open("models/career_model.pkl", "wb"))

print("\nBest Model:", best_model_name)
print("Best Accuracy:", round(best_accuracy, 2))
print("Model Saved Successfully!")