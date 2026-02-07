import os
from moviepy.editor import ImageClip, AudioFileClip
# Import the configuration change utility
from moviepy.config import change_settings 
from src.mixmaster.utils.logger import logger

# --- FFmpeg Manual Path Fix ---
# This ensures MoviePy uses the specific version you downloaded
FFMPEG_PATH = r"C:\\Users\\91901\\Downloads\\ffmpeg\\ffmpeg-2024-12-26-git-fe04b93afa-full_build\\bin\\ffmpeg.exe"
change_settings({"FFMPEG_BINARY": FFMPEG_PATH})
# ------------------------------

class VideoRenderer:
    def __init__(self, fps: int = 5):
        self.fps = fps

    def create_video(self, audio_path: str, image_path: str, output_path: str):
        try:
            logger.info(f"Rendering video: {output_path}")
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            audio_clip = AudioFileClip(audio_path)
            video_clip = (ImageClip(image_path)
                         .set_duration(audio_clip.duration)
                         .set_fps(self.fps))
            
            video_with_audio = video_clip.set_audio(audio_clip)
            
            video_with_audio.write_videofile(
                output_path,
                fps=self.fps,
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
                verbose=False,
                logger=None
            )
            
            # Explicitly close clips to release file locks on Windows
            audio_clip.close()
            video_clip.close()
            video_with_audio.close()
            
            logger.info("Video complete")
            return output_path
        except Exception as e:
            logger.error(f"Video failed: {e}")
            raise