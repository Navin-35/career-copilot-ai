from pydantic import BaseModel


class RoadmapRequest(BaseModel):

    resume_id: int

    target_role: str


class RoadmapResponse(BaseModel):

    roadmap: dict