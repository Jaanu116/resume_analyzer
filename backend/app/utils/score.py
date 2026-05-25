def calculate_score(skills):

    score = 0

    if len(skills) >= 1:
        score += 20

    if len(skills) >= 3:
        score += 20

    if len(skills) >= 5:
        score += 20

    if len(skills) >= 7:
        score += 20

    if len(skills) >= 10:
        score += 20

    return min(score,100)