from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "MixMaster AI"
    UPLOAD_DIR: str = "data/uploads"
    EXPORT_DIR: str = "data/exports"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.EXPORT_DIR, exist_ok=True)
