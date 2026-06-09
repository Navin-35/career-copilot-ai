from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.resume import Resume

from app.schemas.skill_gap import (
    SkillGapRequest
)

from app.services.profile_service import (
    analyze_resume_text
)

from app.services.skill_gap_service import (
    analyze_skill_gap
)

router = APIRouter(
    prefix="/career",
    tags=["Career"]
)


@router.post("/skill-gap")
def skill_gap_analysis(
    request: SkillGapRequest,
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

    profile = analyze_resume_text(
        resume.extracted_text
    )

    result = analyze_skill_gap(
        profile["skills"],
        request.target_role
    )

    return result