def calculate_ats(
    skills,
    sections,
    text
):

    text = text.lower()

    score = 0

    breakdown = {}

    # Skills (40)

    skills_score=min(
        len(skills)*8,
        40
    )

    breakdown["skills_match"]=skills_score

    score+=skills_score


    # Sections (20)

    sections_score=min(
        len(sections)*5,
        20
    )

    breakdown["resume_sections"]=sections_score

    score+=sections_score


    # Keywords (20)

    keywords=[
        "project",
        "internship",
        "machine learning",
        "leadership",
        "certification"
    ]

    count=0

    for word in keywords:

        if word in text:

            count+=1

    keyword_score=min(
        count*4,
        20
    )

    breakdown["keywords"]=keyword_score

    score+=keyword_score


    # Experience relevance (10)

    exp_words=[
        "intern",
        "worked",
        "experience",
        "developer"
    ]

    exp=0

    for word in exp_words:

        if word in text:

            exp+=1

    experience_score=min(
        exp*3,
        10
    )

    breakdown["experience_relevance"]=experience_score

    score+=experience_score


    # Formatting (10)

    formatting=10

    if len(text)<300:

        formatting=5

    breakdown["formatting"]=formatting

    score+=formatting


    return {
        "score":min(score,100),
        "breakdown":breakdown
    }