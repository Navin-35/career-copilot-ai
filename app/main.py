from fastapi import FastAPI
from app.api.user_router import router as user_router
from app.core.config import settings
from app.api.auth_router import router as auth_router
from app.database.database import engine
from app.database.base import Base
from app.api.resume_router import (
    router as resume_router
)
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(resume_router)
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