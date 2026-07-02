KNOWN_SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "SQL",
    "MongoDB",
    "Docker",
    "Git",
    "Machine Learning",
    "HTML",
    "CSS"
]


def extract_skills(text):

    found_skills = []

    for skill in KNOWN_SKILLS:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills