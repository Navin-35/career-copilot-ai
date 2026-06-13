import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.resume_service import (
    extract_resume_text,
    save_resume
)
from app.models.resume import Resume

from app.services.profile_service import (
    analyze_resume_text
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    upload_path = (
        f"uploads/{file.filename}"
    )

    with open(
        upload_path,
        "wb"
    ) as buffer:

        content = await file.read()

        buffer.write(content)

    text = extract_resume_text(
        upload_path
    )

    save_resume(
        db,
        user_id=1,
        file_name=file.filename,
        text=text
    )

    return {
        "message":
        "Resume uploaded successfully"
    }
@router.post(
    "/analyze/{resume_id}"
)
def analyze_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(
            Resume.id == resume_id
        )
        .first()
    )

    if not resume:
        return {
            "error":
            "Resume not found"
        }

    result = analyze_resume_text(
        resume.extracted_text
    )

    return result    