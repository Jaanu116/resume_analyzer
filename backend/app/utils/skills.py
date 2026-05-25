SKILLS = [
    "Python",
    "Java",
    "React",
    "FastAPI",
    "SQL",
    "JavaScript",
    "HTML",
    "CSS",
    "Tailwind",
    "Git",
    "Node"
]

def extract_skills(text):

    found=[]

    text=text.lower()

    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill)

    return found