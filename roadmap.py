roadmaps = {

    "AI Engineer": [
        "Week 1 : Python",
        "Week 2 : Machine Learning",
        "Week 3 : Deep Learning",
        "Week 4 : TensorFlow",
        "Week 5 : PyTorch",
        "Week 6 : Build AI Project",
        "Week 7 : Deploy Project"
    ],

    "ML Engineer": [
        "Week 1 : Python",
        "Week 2 : NumPy & Pandas",
        "Week 3 : Scikit-learn",
        "Week 4 : TensorFlow",
        "Week 5 : Docker",
        "Week 6 : ML Project"
    ],

    "Data Scientist": [
        "Week 1 : Python",
        "Week 2 : Pandas",
        "Week 3 : SQL",
        "Week 4 : Statistics",
        "Week 5 : Machine Learning",
        "Week 6 : Data Science Project"
    ],

    "Cloud Engineer": [
        "Week 1 : Linux",
        "Week 2 : AWS",
        "Week 3 : Docker",
        "Week 4 : Kubernetes",
        "Week 5 : CI/CD",
        "Week 6 : Cloud Project"
    ],

    "Software Engineer": [
        "Week 1 : C++ / Java",
        "Week 2 : Python",
        "Week 3 : SQL",
        "Week 4 : Git",
        "Week 5 : Data Structures",
        "Week 6 : Build Software Project"
    ]
}

def get_roadmap(career):
    return roadmaps.get(career, ["No roadmap available."])