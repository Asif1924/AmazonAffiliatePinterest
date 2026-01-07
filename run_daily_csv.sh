#!/bin/bash

# Amazon Affiliate Pinterest Automation - Daily Runner Script
# This script is designed to be called by cron or launchd

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Set up PATH (important for cron jobs)
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the Python script
python3 daily_canva_csv.py

# Capture exit code
EXIT_CODE=$?

# Optional: Send macOS notification on completion
if command -v osascript &> /dev/null; then
    if [ $EXIT_CODE -eq 0 ]; then
        osascript -e 'display notification "Pinterest CSV generated successfully" with title "Automation Complete"'
    else
        osascript -e 'display notification "Pinterest CSV generation failed" with title "Automation Error"'
    fi
fi

# Exit with the same code as the Python script
exit $EXIT_CODE

