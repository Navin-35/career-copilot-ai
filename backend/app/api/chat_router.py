from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest
)

from app.services.career_chat_service import (
    career_chat
)

router = APIRouter(
    prefix="/career",
    tags=["Career Chat"]
)


@router.post("/ask")
def ask_question(
    request: ChatRequest
):

    answer = career_chat(
        request.question
    )

    return {
        "answer": answer
    }