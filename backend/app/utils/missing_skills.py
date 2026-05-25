REQUIRED_SKILLS = [
    "Python",
    "SQL",
    "Git",
    "FastAPI",
    "React",
    "Docker",
    "JavaScript",
    "Machine Learning"
]


def get_missing_skills(skills):

    missing=[]

    for skill in REQUIRED_SKILLS:

        if skill not in skills:

            missing.append(skill)

    return missing