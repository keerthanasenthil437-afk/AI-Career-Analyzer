projects = {

    "AI Engineer": [
        "Chatbot using LLM",
        "Face Recognition System",
        "AI Resume Analyzer",
        "Image Caption Generator",
        "Voice Assistant"
    ],

    "Data Scientist": [
        "House Price Prediction",
        "Customer Churn Prediction",
        "Movie Recommendation System",
        "Sales Forecasting",
        "Credit Card Fraud Detection"
    ],

    "ML Engineer": [
        "House Price Prediction",
        "Customer Churn Prediction",
        "Movie Recommendation System",
        "Credit Card Fraud Detection",
        "Sales Forecasting"
    ],

    "Software Engineer": [
        "Library Management System",
        "Bank Management System",
        "Student Management System",
        "Hospital Management System",
        "Online Voting System"
    ],

    "Full Stack Developer": [
        "E-Commerce Website",
        "Blog Website",
        "Food Delivery App",
        "Portfolio Website",
        "Chat Application"
    ],

    "Frontend Developer": [
        "Portfolio Website",
        "Netflix Clone",
        "Weather App",
        "To-Do App",
        "Landing Page"
    ],

    "Backend Developer": [
        "REST API",
        "Authentication System",
        "Library Backend",
        "Blog Backend",
        "Inventory API"
    ],

    "Web Developer": [
        "College Website",
        "Restaurant Website",
        "Portfolio Website",
        "E-Commerce Website",
        "Blog Website"
    ],

    "Cloud Engineer": [
        "AWS Deployment",
        "Dockerized Web App",
        "CI/CD Pipeline",
        "Kubernetes Project",
        "Cloud Monitoring System"
    ],

    "Data Analyst": [
        "Sales Dashboard",
        "COVID Data Analysis",
        "IPL Data Analysis",
        "HR Dashboard",
        "Financial Dashboard"
    ]

}

def get_projects(career):
    return projects.get(career, ["No recommendations available."])