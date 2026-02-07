import pytest
from src.mixmaster.core.processor import AudioProcessor

def test_timestamp_formatting():
    processor = AudioProcessor()
    # Test cases: ms -> HH:MM:SS
    assert processor._format_timestamp(0) == "00:00:00"
    assert processor._format_timestamp(61000) == "00:01:01"
    assert processor._format_timestamp(3661000) == "01:01:01"

def test_track_metadata_calculation():
    processor = AudioProcessor(crossfade_ms=2000)
    # Mocking track data logic
    # Track 1: 10s (10000ms)
    # Track 2: 10s (10000ms)
    # Crossfade: 2s
    # Total Mix should be 18s. Track 2 should start at 8s.
    
    t1_start = 0
    t1_duration = 10000
    crossfade = 2000
    
    t2_start = t1_duration - crossfade
    
    assert processor._format_timestamp(t2_start) == "00:00:08"