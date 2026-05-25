def detect_sections(text):

    text=text.lower()

    sections=[]

    keywords=[
        "education",
        "experience",
        "projects",
        "skills",
        "certifications"
    ]

    for word in keywords:

        if word in text:

            sections.append(word)

    return sections