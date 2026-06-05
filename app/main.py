from fastapi import FastAPI

from app.core.config import settings

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