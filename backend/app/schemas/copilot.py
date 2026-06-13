from pydantic import BaseModel


class CopilotRequest(BaseModel):

    resume_id: int

    target_role: str