from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.resume import Resume

from app.schemas.roadmap import (
    RoadmapRequest
)

from app.services.profile_service import (
    analyze_resume_text
)

from app.services.skill_gap_service import (
    analyze_skill_gap
)

from app.services.roadmap_service import (
    generate_learning_roadmap
)

router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)


@router.post("/generate")
def generate_roadmap(
    request: RoadmapRequest,
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
            "error": "Resume not found"
        }

    profile = analyze_resume_text(
        resume.extracted_text
    )

    gap = analyze_skill_gap(
        profile["skills"],
        request.target_role
    )

    roadmap = generate_learning_roadmap(
        profile["skills"],
        gap["missing_skills"],
        request.target_role
    )

    return roadmap