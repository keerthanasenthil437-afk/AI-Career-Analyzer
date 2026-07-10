roadmaps = {

    "AI Engineer": [
        "Week 1 : Python",
        "Week 2 : Machine Learning",
        "Week 3 : Deep Learning",
        "Week 4 : TensorFlow & PyTorch",
        "Week 5 : NLP & Computer Vision",
        "Week 6 : AI Project"
    ],

    "Data Scientist": [
        "Week 1 : Python",
        "Week 2 : NumPy & Pandas",
        "Week 3 : Data Visualization",
        "Week 4 : Scikit-learn",
        "Week 5 : Machine Learning",
        "Week 6 : Data Science Project"
    ],

    "ML Engineer": [
        "Week 1 : Python",
        "Week 2 : NumPy & Pandas",
        "Week 3 : Scikit-learn",
        "Week 4 : TensorFlow",
        "Week 5 : Docker",
        "Week 6 : ML Project"
    ],

    "Software Engineer": [
        "Week 1 : C & C++",
        "Week 2 : Java",
        "Week 3 : Data Structures",
        "Week 4 : OOP",
        "Week 5 : SQL & Git",
        "Week 6 : Software Project"
    ],

    "Full Stack Developer": [
        "Week 1 : HTML & CSS",
        "Week 2 : JavaScript",
        "Week 3 : React",
        "Week 4 : NodeJS",
        "Week 5 : MongoDB",
        "Week 6 : Full Stack Project"
    ],

    "Frontend Developer": [
        "Week 1 : HTML",
        "Week 2 : CSS",
        "Week 3 : JavaScript",
        "Week 4 : React",
        "Week 5 : Bootstrap",
        "Week 6 : Frontend Project"
    ],

    "Backend Developer": [
        "Week 1 : Python",
        "Week 2 : Flask",
        "Week 3 : Django",
        "Week 4 : FastAPI",
        "Week 5 : SQL & MongoDB",
        "Week 6 : Backend Project"
    ],

    "Web Developer": [
        "Week 1 : HTML",
        "Week 2 : CSS",
        "Week 3 : JavaScript",
        "Week 4 : PHP",
        "Week 5 : MySQL",
        "Week 6 : Web Project"
    ],

    "Cloud Engineer": [
        "Week 1 : Linux",
        "Week 2 : AWS",
        "Week 3 : Azure",
        "Week 4 : Docker",
        "Week 5 : Kubernetes",
        "Week 6 : Cloud Project"
    ],

    "Data Analyst": [
        "Week 1 : Excel",
        "Week 2 : SQL",
        "Week 3 : Python",
        "Week 4 : Pandas",
        "Week 5 : Power BI",
        "Week 6 : Dashboard Project"
    ]

}

def get_roadmap(career):
    return roadmaps.get(career, ["No roadmap available."])