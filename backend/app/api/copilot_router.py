from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.resume import Resume

from app.schemas.copilot import (
    CopilotRequest
)

from app.agents.career_graph import (
    career_graph
)

router = APIRouter(
    prefix="/copilot",
    tags=["Career Copilot"]
)


@router.post("/run")
def run_copilot(
    request: CopilotRequest,
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(
            Resume.id == request.resume_id
        )
        .first()
    )

    state = {

        "resume_text":
        resume.extracted_text,

        "target_role":
        request.target_role,

        "profile": {},

        "skill_gap": {},

        "roadmap": {},

        "final_response": ""
    }

    result = career_graph.invoke(
        state
    )

    return result["final_response"]