from pydantic import BaseModel
from typing import List

class MixtapeResponse(BaseModel):
    message: str
    audio_url: str
    video_url: str
    tracklist: List[str]

class ErrorResponse(BaseModel):
    detail: str