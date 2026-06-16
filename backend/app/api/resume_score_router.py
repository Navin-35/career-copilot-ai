from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.session import (
    get_db
)

from app.schemas.resume_score import (
    ResumeScoreRequest
)

from app.services.resume_score_service import (
    generate_resume_score
)

router = APIRouter(
    prefix="/career",
    tags=["Resume Score"]
)


@router.post(
    "/resume-score"
)
def resume_score(
    request: ResumeScoreRequest,
    db: Session = Depends(get_db)
):

    return generate_resume_score(
        db,
        request.resume_id,
        request.target_role
    )