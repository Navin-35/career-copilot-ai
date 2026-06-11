from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.state import (
    CareerState
)

from app.agents.resume_agent import (
    resume_agent
)

from app.agents.skill_gap_agent import (
    skill_gap_agent
)

from app.agents.roadmap_agent import (
    roadmap_agent
)

from app.agents.career_coach_agent import (
    career_coach_agent
)


graph = StateGraph(
    CareerState
)

graph.add_node(
    "resume",
    resume_agent
)

graph.add_node(
    "skill_gap",
    skill_gap_agent
)

graph.add_node(
    "roadmap",
    roadmap_agent
)

graph.add_node(
    "coach",
    career_coach_agent
)

graph.set_entry_point(
    "resume"
)

graph.add_edge(
    "resume",
    "skill_gap"
)

graph.add_edge(
    "skill_gap",
    "roadmap"
)

graph.add_edge(
    "roadmap",
    "coach"
)

graph.add_edge(
    "coach",
    END
)

career_graph = graph.compile()