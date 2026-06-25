def calculate_ats_score(resume_text):

    required_skills = [
        "Python",
        "JavaScript",
        "React",
        "SQL"
    ]

    matched_skills = []

    for skill in required_skills:

        if skill.lower() in resume_text.lower():

            matched_skills.append(skill)

    score = (
        len(matched_skills)
        /
        len(required_skills)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": list(
            set(required_skills)
            - set(matched_skills)
        )
    }