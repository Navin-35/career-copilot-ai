from app.services.skill_gap_service import (
    analyze_skill_gap
)


def skill_gap_agent(
    state
):

    gap = analyze_skill_gap(
        state["profile"]["skills"],
        state["target_role"]
    )

    state["skill_gap"] = gap

    return state