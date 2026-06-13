from app.services.profile_service import (
    analyze_resume_text
)


def resume_agent(
    state
):

    profile = analyze_resume_text(
        state["resume_text"]
    )

    state["profile"] = profile

    return state