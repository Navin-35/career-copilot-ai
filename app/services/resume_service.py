import fitz

from sqlalchemy.orm import Session

from app.models.resume import Resume


def extract_resume_text(
    file_path: str
):

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    return text


def save_resume(
    db: Session,
    user_id: int,
    file_name: str,
    text: str
):

    resume = Resume(
        user_id=user_id,
        file_name=file_name,
        extracted_text=text
    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume