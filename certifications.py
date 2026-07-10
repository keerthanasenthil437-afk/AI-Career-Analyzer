certifications = {

    "AI Engineer": [
        "DeepLearning.AI TensorFlow Developer",
        "IBM AI Engineering",
        "Google AI Essentials"
    ],

    "Data Scientist": [
        "IBM Data Science Professional Certificate",
        "Google Advanced Data Analytics",
        "Machine Learning by Andrew Ng"
    ],

    "ML Engineer": [
        "Machine Learning by Andrew Ng (Coursera)",
        "IBM Machine Learning Professional Certificate",
        "AWS Machine Learning Specialty"
    ],

    "Software Engineer": [
        "CS50 by Harvard",
        "Python for Everybody",
        "Oracle Java Foundations"
    ],

    "Full Stack Developer": [
        "Meta Full Stack Developer",
        "The Complete Web Development Bootcamp",
        "MongoDB Developer"
    ],

    "Frontend Developer": [
        "Meta Front-End Developer",
        "Responsive Web Design",
        "JavaScript Algorithms"
    ],

    "Backend Developer": [
        "Django for Everybody",
        "REST API Development",
        "NodeJS Certification"
    ],

    "Web Developer": [
        "Responsive Web Design",
        "PHP for Beginners",
        "JavaScript Certification"
    ],

    "Cloud Engineer": [
        "AWS Cloud Practitioner",
        "Microsoft Azure Fundamentals",
        "Google Cloud Associate Engineer"
    ],

    "Data Analyst": [
        "Google Data Analytics",
        "Microsoft Power BI",
        "IBM Data Analyst"
    ]

}

def get_certifications(career):
    return certifications.get(career, ["No certifications available."])