import os
from dataclasses import dataclass
from typing import List

from pydub import AudioSegment
from pydub.effects import normalize  # NEW


@dataclass
class TrackMetadata:
    name: str
    start_time: str  # Format: 00:00:00
    duration_ms: int


class AudioProcessor:
    def __init__(self, crossfade_ms: int = 2000):
        self.crossfade_ms = crossfade_ms
        self.metadata: List[TrackMetadata] = []

    def _format_timestamp(self, ms: int) -> str:
        """Converts milliseconds to HH:MM:SS format."""
        seconds = (ms // 1000) % 60
        minutes = (ms // (1000 * 60)) % 60
        hours = (ms // (1000 * 60 * 60)) % 24
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def create_mixtape(
        self,
        audio_paths: List[str],
        output_path: str,
    ) -> List[TrackMetadata]:
        if not audio_paths:
            raise ValueError("No audio files provided.")

        # First track (normalize)
        first_track = AudioSegment.from_file(audio_paths[0])
        first_track = normalize(first_track)

        combined = first_track

        self.metadata.append(
            TrackMetadata(
                name=os.path.basename(audio_paths[0]),
                start_time=self._format_timestamp(0),
                duration_ms=len(combined),
            )
        )

        current_duration = len(combined)

        for path in audio_paths[1:]:
            next_track = AudioSegment.from_file(path)
            next_track = normalize(next_track)  # NEW: consistent loudness

            start_ms = current_duration - self.crossfade_ms

            self.metadata.append(
                TrackMetadata(
                    name=os.path.basename(path),
                    start_time=self._format_timestamp(start_ms),
                    duration_ms=len(next_track),
                )
            )

            combined = combined.append(next_track, crossfade=self.crossfade_ms)
            current_duration = len(combined)

        combined.export(output_path, format="mp3", bitrate="320k")
        return self.metadata
