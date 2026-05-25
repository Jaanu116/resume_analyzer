def calculate_score(skills, sections):

    score = 0

    # Skills score (max 50)
    score += min(len(skills) * 10, 50)

    # Section score (max 50)
    score += min(len(sections) * 10, 50)

    return min(score, 100)