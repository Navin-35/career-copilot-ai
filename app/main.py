from fastapi import FastAPI
from app.api.user_router import router as user_router
from app.core.config import settings
from app.api.auth_router import router as auth_router
from app.database.database import engine
from app.database.base import Base
from app.api.resume_router import (
    router as resume_router
)
from app.api.career_router import (router as career_router)
import app.models
from app.api.roadmap_router import (router as roadmap_router)
from app.api.chat_router import (router as chat_router)
from app.api.copilot_router import (
    router as copilot_router
)
from app.api.copilot_chat_router import (
    router as copilot_chat_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(career_router)
app.include_router(roadmap_router)
app.include_router(chat_router)
app.include_router(
    copilot_router
)
app.include_router(
    copilot_chat_router
)

@app.get("/")
def home():
    return {
        "message": "Career Copilot API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }