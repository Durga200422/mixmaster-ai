from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Absolute imports because main.py is in the root
from src.mixmaster.api.routes import router
from src.mixmaster.utils.settings import settings

app = FastAPI(title=settings.APP_NAME, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}