from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.resume import Resume

from app.schemas.copilot_chat import (
    CopilotChatRequest
)

from app.services.copilot_chat_service import (
    run_copilot_chat
)

router = APIRouter(
    prefix="/copilot",
    tags=["Agentic Copilot"]
)


@router.post("/chat")
def chat(
    request: CopilotChatRequest,
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(
            Resume.id == request.resume_id
        )
        .first()
    )

    if not resume:

        return {
            "error":
            "Resume not found"
        }

    return run_copilot_chat(
        request.question,
        resume,
        request.target_role
    )