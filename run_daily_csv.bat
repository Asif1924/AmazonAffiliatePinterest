@echo off
REM Amazon Affiliate Pinterest Automation - Daily Runner Script (Windows)
REM This script is designed to be called by Windows Task Scheduler

REM Get the directory where this script is located
cd /d %~dp0

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Run the Python script
python daily_canva_csv.py

REM Capture exit code
set EXIT_CODE=%ERRORLEVEL%

REM Exit with the same code as the Python script
exit /b %EXIT_CODE%

