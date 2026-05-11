@echo off
setlocal
cd /d "%~dp0"

where mkdocs >nul 2>nul
if errorlevel 1 (
  echo [ERROR] mkdocs is not installed in the active environment.
  echo         Set up the environment first:
  echo         conda env create -f environment.yml ^&^& conda activate diem-validation
  exit /b 1
)

echo [INFO] Starting local documentation server at http://127.0.0.1:8000/
start "" "http://127.0.0.1:8000/"
mkdocs serve
