import os
import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
# Inside src/mixmaster/api/routes.py
from src.mixmaster.core.processor import AudioProcessor 
from src.mixmaster.core.renderer import VideoRenderer
from src.mixmaster.utils.settings import settings 
from src.mixmaster.utils.logger import logger
from src.mixmaster.utils.cleanup import cleanup_old_files

router = APIRouter()

@router.post("/create-mixtape")
async def create_mixtape_endpoint(
    background_tasks: BackgroundTasks,
    audio_files: list[UploadFile] = File(...),
    image_file: UploadFile = File(...),
):
    session_id = str(uuid.uuid4())
    session_dir = Path(settings.UPLOAD_DIR) / session_id
    session_dir.mkdir(exist_ok=True, parents=True) # Added parents=True for safety

    try:
        saved_audio_paths = []
        for file in audio_files:
            # Added common variations of audio mime types
            if file.content_type not in ['audio/mpeg', 'audio/wav', 'audio/x-wav', 'audio/mp3']:
                raise HTTPException(400, f"Invalid audio format: {file.content_type}")
            
            path = session_dir / file.filename
            with open(path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_audio_paths.append(str(path))

        if image_file.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise HTTPException(400, "Invalid image format")
            
        image_path = session_dir / image_file.filename
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image_file.file, buffer)

        # 1. Process Audio
        processor = AudioProcessor(crossfade_ms=2000)
        output_audio = Path(settings.EXPORT_DIR) / f"{session_id}.mp3"
        metadata = processor.create_mixtape(saved_audio_paths, str(output_audio))

        # 2. Render Video (Synchronous call so Streamlit waits)
        output_video = Path(settings.EXPORT_DIR) / f"{session_id}.mp4"
        renderer = VideoRenderer(fps=5)
        
        # We call this directly instead of background_tasks
        renderer.create_video(str(output_audio), str(image_path), str(output_video))
        
        # Cleanup remains a background task
        background_tasks.add_task(cleanup_old_files, 24)
        
        tracklist_text = [f"{m.start_time} - {m.name}" for m in metadata]

        logger.info(f"Mixtape {session_id} created successfully")
        return {
            "status": "success",
            "audio_path": str(output_audio),
            "video_path": str(output_video),
            "youtube_description": tracklist_text,
            "session_id": session_id,
        }
    except Exception as e:
        logger.error(f"Mixtape failed: {e}")
        raise HTTPException(500, str(e))