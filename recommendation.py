projects = {

    "AI Engineer": [
        "Plant Disease Detection",
        "Fake News Detection",
        "Resume Screening",
        "Chatbot using LLM",
        "Object Detection"
    ],

    "ML Engineer": [
        "House Price Prediction",
        "Customer Churn Prediction",
        "Movie Recommendation System",
        "Credit Card Fraud Detection",
        "Sales Forecasting"
    ],

    "Data Scientist": [
        "Stock Market Analysis",
        "Sales Dashboard",
        "Customer Segmentation",
        "Sentiment Analysis",
        "Data Visualization Dashboard"
    ],

    "Data Analyst": [
        "Power BI Sales Dashboard",
        "HR Analytics Dashboard",
        "COVID Data Analysis",
        "Netflix Data Analysis",
        "E-commerce Dashboard"
    ],

    "Cloud Engineer": [
        "AWS Web Application Deployment",
        "Dockerized Flask App",
        "Kubernetes Cluster",
        "CI/CD Pipeline",
        "Cloud Monitoring Dashboard"
    ],

    "Software Engineer": [
        "Library Management System",
        "Hospital Management System",
        "Student Management System",
        "Bank Management System",
        "Online Quiz System"
    ]
}

def get_projects(career):
    return projects.get(career, ["No recommendations available."])