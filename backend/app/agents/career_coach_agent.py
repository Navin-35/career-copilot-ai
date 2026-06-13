def career_coach_agent(
    state
):

    state["final_response"] = {
        "profile":
        state["profile"],

        "skill_gap":
        state["skill_gap"],

        "roadmap":
        state["roadmap"]
    }

    return state