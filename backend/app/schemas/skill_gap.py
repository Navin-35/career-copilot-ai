from pydantic import BaseModel


class SkillGapRequest(BaseModel):

    resume_id: int

    target_role: str


class SkillGapResponse(BaseModel):

    current_skills: list[str]

    missing_skills: list[str]

    recommendations: list[str]