from fastapi import FastAPI

app = FastAPI(
    title="Blood Report Analyzer API",
    version="1.0.0",
    description="Backend API for AI-powered Blood Report Analyzer"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to Blood Report Analyzer Backend!"
    }


@app.get("/health")
def health():
    return {
        "server": "Healthy",
        "backend": "FastAPI",
        "version": "1.0.0"
    }