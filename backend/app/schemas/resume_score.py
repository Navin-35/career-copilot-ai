from pydantic import BaseModel


class ResumeScoreRequest(
    BaseModel
):
    resume_id: int
    target_role: str