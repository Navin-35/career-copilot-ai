from fastapi import FastAPI

app = FastAPI(
    title="Career Copilot API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Career Copilot Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }