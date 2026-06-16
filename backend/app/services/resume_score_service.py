import json

from sqlalchemy.orm import Session

from app.services.resume_service import (
    get_resume
)

from app.services.profile_service import (
    analyze_resume_text
)


def generate_resume_score(
    db: Session,
    resume_id: int,
    target_role: str
):

    resume = get_resume(
        db,
        resume_id
    )

    if not resume:

        return {
            "error": "Resume not found"
        }

    resume_text = (
        resume.extracted_text
        .lower()
    )
    skill_prompt = f"""
You are a career expert.

List the top 10 most important technical skills required for:

{target_role}

Return ONLY JSON.

Example:

{{
    "skills": [
        "Python",
        "TensorFlow",
        "Docker"
    ]
}}
"""

    skill_response = (
        analyze_resume_text(
            skill_prompt
        )
    )

    try:

        skills_json = json.loads(
            skill_response
        )

        required_skills = (
            skills_json["skills"]
        )

    except:

        required_skills = [
            "Python"
        ]
    strengths = []

    missing_skills = []

    found_count = 0

    for skill in required_skills:

        if (
            skill.lower()
            in resume_text
        ):

            strengths.append(
                skill
            )

            found_count += 1

        else:

            missing_skills.append(
                skill
            )
    score = int(

        (
            found_count
            /
            len(required_skills)
        )

        * 100
    )
    recommendations = []

    for skill in missing_skills[:5]:

        recommendations.append(
            f"Learn {skill}"
        )
    return {

        "target_role":
            target_role,

        "score":
            score,

        "required_skills":
            required_skills,

        "strengths":
            strengths,

        "missing_skills":
            missing_skills,

        "recommendations":
            recommendations
    }                                    
    