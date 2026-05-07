@echo off
setlocal

if "%CONDA_PREFIX%"=="" (
  echo [ERROR] No active conda environment detected.
  echo         Activate your environment first, then run this script.
  exit /b 1
)

set "TARGET=%CONDA_PREFIX%\Scripts\documentation.cmd"
copy /Y "%~dp0documentation.cmd" "%TARGET%" >nul
if errorlevel 1 (
  echo [ERROR] Failed to install documentation command to:
  echo         %TARGET%
  exit /b 1
)

echo [OK] Installed documentation command to:
 echo      %TARGET%
echo [OK] In this activated conda environment, you can now run:
 echo      documentation
