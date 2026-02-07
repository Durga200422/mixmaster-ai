import os
import shutil
from mixmaster.utils.settings import settings

def cleanup_old_files(hours_old: int = 24):
    """Delete files older than specified hours (stub for production cron)."""
    import time
    cutoff = time.time() - (hours_old * 3600)
    for dirpath in [settings.UPLOAD_DIR, settings.EXPORT_DIR]:
        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            if os.path.getmtime(filepath) < cutoff:
                try:
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    else:
                        shutil.rmtree(filepath)
                except Exception:
                    pass
