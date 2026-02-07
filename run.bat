@echo off
REM Change to project directory (current folder)
cd /d "%~dp0"

REM Start FastAPI backend - Pointing to main.py in the root
start "mixmaster-api" cmd /c "uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

REM Small delay so API starts before UI
timeout /t 3 >nul

REM Start Streamlit frontend
start "mixmaster-ui" cmd /c "uv run streamlit run src/mixmaster/ui/app.py --server.port 8501"