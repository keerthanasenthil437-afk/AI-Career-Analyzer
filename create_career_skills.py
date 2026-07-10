import pandas as pd

data = {
    "Career": [
        "AI Engineer",
        "Data Scientist",
        "ML Engineer",
        "Software Engineer",
        "Full Stack Developer",
        "Frontend Developer",
        "Backend Developer",
        "Web Developer",
        "Cloud Engineer",
        "Data Analyst"
    ],

    "Skills": [
        "Python,Machine Learning,Deep Learning,Artificial Intelligence,TensorFlow,PyTorch,Scikit-learn,SQL,Git,Docker",
        "Python,SQL,Machine Learning,Pandas,NumPy,Scikit-learn,Matplotlib,Seaborn,Power BI,Excel",
        "Python,Machine Learning,Scikit-learn,TensorFlow,PyTorch,SQL,Git,Docker",
        "Python,Java,C,C++,SQL,Git,GitHub,Linux",
        "HTML,CSS,JavaScript,React,NodeJS,MongoDB,MySQL,Git,GitHub,Bootstrap",
        "HTML,CSS,JavaScript,React,Bootstrap,Git",
        "Python,SQL,NodeJS,Flask,Django,FastAPI,MongoDB,MySQL,Git",
        "HTML,CSS,JavaScript,PHP,Bootstrap,MySQL,Git",
        "Python,AWS,Azure,Docker,Kubernetes,Linux,Git",
        "SQL,Excel,Power BI,Python,Pandas,Data Analysis,Data Visualization,Matplotlib"
    ]
}

df = pd.DataFrame(data)

df.to_csv("datasets/career_skills.csv", index=False)

print("career_skills.csv created successfully!")




import pandas as pd

df = pd.read_csv("datasets/career_skills.csv")
print(df.columns)