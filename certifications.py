certifications = {

    "AI Engineer": [
        "IBM AI Engineering Professional Certificate",
        "Google AI Essentials",
        "AWS Machine Learning Specialty"
    ],

    "ML Engineer": [
        "Machine Learning by Andrew Ng (Coursera)",
        "IBM Machine Learning Professional Certificate",
        "AWS Machine Learning Specialty"
    ],

    "Data Scientist": [
        "IBM Data Science Professional Certificate",
        "Google Data Analytics Certificate",
        "Microsoft Azure Data Scientist Associate"
    ],

    "Cloud Engineer": [
        "AWS Certified Solutions Architect",
        "Microsoft Azure Administrator",
        "Google Associate Cloud Engineer"
    ],

    "Software Engineer": [
        "Meta Back-End Developer",
        "Oracle Java Certification",
        "Microsoft Azure Developer Associate"
    ]
}

def get_certifications(career):
    return certifications.get(career, ["No certifications available."])