from app.services.profile_service import (
    analyze_resume_text
)

from app.services.skill_gap_service import (
    analyze_skill_gap
)

from app.services.roadmap_service import (
    generate_learning_roadmap
)

from app.services.career_chat_service import (
    career_chat
)

from app.agents.supervisor_agent import (
    supervisor_agent
)


def run_copilot_chat(
    question,
    resume,
    target_role
):

    decision = supervisor_agent(
        question
    )
    print("Supervisor Decision:", decision)
    if "resume" in decision:

        return analyze_resume_text(
            resume.extracted_text
        )

    elif "skill" in decision:

        profile = analyze_resume_text(
            resume.extracted_text
        )

        return analyze_skill_gap(
            profile["skills"],
            target_role
        )

    elif "roadmap" in decision:

        profile = analyze_resume_text(
            resume.extracted_text
        )

        gap = analyze_skill_gap(
            profile["skills"],
            target_role
        )

        return generate_learning_roadmap(
            profile["skills"],
            gap["missing_skills"],
            target_role
        )

    else:

        return {
            "answer":
            career_chat(question)
        }