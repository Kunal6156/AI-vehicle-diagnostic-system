@echo off
REM Alto Car Digital Manual - Quick Setup Script for Windows

echo ================================================
echo Alto Car Digital Manual - Setup Script
echo ================================================
echo.

REM Check Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
echo Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Dependencies installed
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo .env file created
    echo.
    echo WARNING: Edit .env file and add your API keys!
    echo.
) else (
    echo .env file already exists
    echo.
)

REM Create uploads directory
echo Creating uploads directory...
if not exist static\uploads mkdir static\uploads
echo Uploads directory created
echo.

echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your API keys:
echo    - GEMINI_API_KEY
echo    - YOUTUBE_API_KEY
echo.
echo 2. Run the application:
echo    python app.py
echo.
echo 3. Open browser and go to:
echo    http://localhost:5000
echo.
echo ================================================
pause
