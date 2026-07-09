from skill_gap import analyze_skill_gap

def calculate_readiness(career, skills):

    required, missing = analyze_skill_gap(career, skills)

    if len(required) == 0:
        return 0

    readiness = ((len(required) - len(missing))
                 / len(required)) * 100

    return round(readiness, 2)