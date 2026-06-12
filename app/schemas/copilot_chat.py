from pydantic import BaseModel


class CopilotChatRequest(BaseModel):

    question: str

    resume_id: int

    target_role: str