import fitz

from sqlalchemy.orm import Session

from app.models.resume import Resume


def extract_resume_text(file_path: str):

    text = ""

    pdf = fitz.open(file_path)

    for page_num in range(len(pdf)):

        page = pdf.load_page(page_num)

        page_text = page.get_text("text")

        print("PAGE TEXT:")
        print(page_text)

        text += page_text

    pdf.close()

    return text.strip()


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