from fastapi import FastAPI

from app.core.config import settings

from app.database.database import engine
from app.database.base import Base

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
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