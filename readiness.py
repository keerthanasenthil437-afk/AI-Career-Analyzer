from skill_gap import analyze_skill_gap


def calculate_readiness(career, skills):

    required, missing = analyze_skill_gap(career, skills)

    # No required skills available
    if len(required) == 0:
        return 0, 0, 0

    # Skills that are already present
    matched = len(required) - len(missing)

    # Readiness percentage
    readiness = (matched / len(required)) * 100

    return (
        round(readiness, 2),
        matched,
        len(missing)
    )