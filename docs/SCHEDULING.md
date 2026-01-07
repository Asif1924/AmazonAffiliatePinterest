# Scheduling Guide

This guide explains how to schedule the `daily_canva_csv.py` script to run automatically every day.

## Prerequisites

- Python script is working correctly (test it manually first)
- All dependencies are installed
- Configuration is complete

## Option 1: macOS/Linux (cron)

### Step 1: Test the script path

```bash
# Find the full path to Python
which python3

# Test running the script
cd /path/to/AmazonAffiliatePinterest
python3 daily_canva_csv.py
```

### Step 2: Create a shell wrapper script

Create a file `run_daily_csv.sh`:

```bash
#!/bin/bash

# Change to script directory
cd /Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest

# Activate virtual environment (if using one)
# source venv/bin/activate

# Run the script
/usr/bin/python3 daily_canva_csv.py

# Optional: Send notification on completion
# osascript -e 'display notification "Pinterest CSV generated" with title "Automation Complete"'
```

Make it executable:
```bash
chmod +x run_daily_csv.sh
```

### Step 3: Edit crontab

```bash
crontab -e
```

Add this line to run daily at 9:00 AM:
```
0 9 * * * /Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest/run_daily_csv.sh >> /Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest/logs/cron.log 2>&1
```

### Cron Schedule Examples

```
# Every day at 9:00 AM
0 9 * * *

# Every day at 6:00 AM
0 6 * * *

# Every weekday at 8:00 AM
0 8 * * 1-5

# Every Monday at 10:00 AM
0 10 * * 1

# Twice daily (9 AM and 5 PM)
0 9,17 * * *
```

### Step 4: Verify cron job

```bash
# List your cron jobs
crontab -l

# Check cron logs (macOS)
log show --predicate 'process == "cron"' --last 1h

# Check your script logs
tail -f logs/cron.log
```

## Option 2: Windows (Task Scheduler)

### Step 1: Create a batch file

Create `run_daily_csv.bat`:

```batch
@echo off
cd /d C:\Users\YourUsername\Projects\AIProjects\AmazonAffiliatePinterest

REM Activate virtual environment (if using one)
REM call venv\Scripts\activate.bat

python daily_canva_csv.py >> logs\task_scheduler.log 2>&1
```

### Step 2: Open Task Scheduler

1. Press `Win + R`
2. Type `taskschd.msc`
3. Press Enter

### Step 3: Create a new task

1. Click "Create Basic Task" in the right panel
2. Name: "Pinterest CSV Generator"
3. Description: "Generates daily Canva CSV for Pinterest pins"
4. Click "Next"

### Step 4: Set trigger

1. Select "Daily"
2. Click "Next"
3. Set start time (e.g., 9:00 AM)
4. Set recur every: 1 days
5. Click "Next"

### Step 5: Set action

1. Select "Start a program"
2. Click "Next"
3. Program/script: Browse to `run_daily_csv.bat`
4. Start in: `C:\Users\YourUsername\Projects\AIProjects\AmazonAffiliatePinterest`
5. Click "Next"

### Step 6: Configure settings

1. Check "Open the Properties dialog for this task when I click Finish"
2. Click "Finish"
3. In Properties:
   - Check "Run whether user is logged on or not"
   - Check "Run with highest privileges"
   - Configure for: Windows 10
4. Click "OK"

### Step 7: Test the task

1. Right-click the task
2. Click "Run"
3. Check the logs folder for output

## Option 3: macOS (launchd) - More Reliable than cron

### Step 1: Create a plist file

Create `~/Library/LaunchAgents/com.pinterest.csvgenerator.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.pinterest.csvgenerator</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>/Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest/run_daily_csv.sh</string>
    </array>
    
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    
    <key>StandardOutPath</key>
    <string>/Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest/logs/launchd.log</string>
    
    <key>StandardErrorPath</key>
    <string>/Users/yourusername/Projects/AIProjects/AmazonAffiliatePinterest/logs/launchd_error.log</string>
</dict>
</plist>
```

### Step 2: Load the launch agent

```bash
launchctl load ~/Library/LaunchAgents/com.pinterest.csvgenerator.plist
```

### Step 3: Verify it's loaded

```bash
launchctl list | grep pinterest
```

### Step 4: Test it manually

```bash
launchctl start com.pinterest.csvgenerator
```

### Step 5: Unload (if needed)

```bash
launchctl unload ~/Library/LaunchAgents/com.pinterest.csvgenerator.plist
```

## Troubleshooting

### Script doesn't run

1. Check file permissions: `ls -l daily_canva_csv.py`
2. Check Python path: `which python3`
3. Test script manually: `python3 daily_canva_csv.py`
4. Check logs in `logs/` directory

### Environment variables not available

Add to your wrapper script:
```bash
export PATH=/usr/local/bin:/usr/bin:/bin
source ~/.bashrc  # or ~/.zshrc
```

### Virtual environment issues

Make sure to activate it in the wrapper script:
```bash
source /path/to/venv/bin/activate
```

### Permission denied

```bash
chmod +x run_daily_csv.sh
chmod +x daily_canva_csv.py
```

## Monitoring

### Check if it ran today

```bash
ls -lt daily_csv/
```

### View recent logs

```bash
tail -50 logs/pinterest_automation.log
```

### Get email notifications (Linux/macOS)

Add to crontab:
```
MAILTO=your.email@example.com
0 9 * * * /path/to/run_daily_csv.sh
```

## Best Practices

1. **Test manually first** - Always test the script before scheduling
2. **Use absolute paths** - Never rely on relative paths in scheduled tasks
3. **Log everything** - Redirect output to log files
4. **Monitor regularly** - Check logs weekly to ensure it's working
5. **Set up alerts** - Get notified if the script fails
6. **Keep credentials secure** - Never commit credentials to version control

