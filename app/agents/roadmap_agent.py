from app.services.roadmap_service import (
    generate_learning_roadmap
)


def roadmap_agent(
    state
):

    roadmap = generate_learning_roadmap(
        state["profile"]["skills"],
        state["skill_gap"]["missing_skills"],
        state["target_role"]
    )

    state["roadmap"] = roadmap

    return state