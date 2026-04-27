@echo off
cd /d "%~dp0"
setlocal

echo ============================
echo      Starting Flask App
echo ============================

:: Set virtual environment folder
set VENV_DIR=venv

:: Create virtual environment if missing
if not exist "%VENV_DIR%\Scripts\activate" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate virtual environment
call %VENV_DIR%\Scripts\activate

:: Upgrade pip (optional but good practice)
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Start Flask app
echo Launching Flask server...
start "" python app.py

:: Wait for server to initialize
timeout /t 5 >nul

:: Open browser
start http://localhost:5000

echo App is running.
pause
