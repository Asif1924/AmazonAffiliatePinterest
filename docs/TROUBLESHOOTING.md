# Troubleshooting Guide

Common issues and their solutions.

## Installation Issues

### "Python 3 not found"

**Problem**: `python3: command not found`

**Solution**:
- Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
- On macOS: `brew install python3`
- On Ubuntu/Debian: `sudo apt-get install python3`

### "pip install fails"

**Problem**: Errors during `pip install -r requirements.txt`

**Solution**:
```bash
# Upgrade pip first
pip install --upgrade pip

# Try installing again
pip install -r requirements.txt

# If still failing, install packages one by one
pip install google-auth gspread openai
```

## Configuration Issues

### "config.py not found"

**Problem**: `ImportError: No module named 'config'`

**Solution**:
```bash
cp config.example.py config.py
# Then edit config.py with your settings
```

### "Invalid API key"

**Problem**: `AuthenticationError: Invalid API key`

**Solution**:
- Check your API key in `config.py`
- Make sure there are no extra spaces or quotes
- Verify the key is active in your provider's dashboard
- For OpenAI: Check at https://platform.openai.com/api-keys
- For Anthropic: Check at https://console.anthropic.com/

## Google Sheets Issues

### "Credentials file not found"

**Problem**: `FileNotFoundError: credentials/google_service_account.json`

**Solution**:
1. Download your service account JSON from Google Cloud Console
2. Save it as `credentials/google_service_account.json`
3. Make sure the path in `config.py` matches

### "Permission denied" on Google Sheets

**Problem**: `gspread.exceptions.APIError: PERMISSION_DENIED`

**Solution**:
1. Open your Google Sheet
2. Click "Share"
3. Add the service account email (found in your JSON file)
4. Give it "Editor" permissions
5. Click "Send"

### "Sheet not found"

**Problem**: `gspread.exceptions.SpreadsheetNotFound`

**Solution**:
- Check your `GOOGLE_SHEET_ID` in `config.py`
- Get it from the URL: `https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit`
- Make sure the sheet is shared with your service account

### "Worksheet not found"

**Problem**: `gspread.exceptions.WorksheetNotFound: Products`

**Solution**:
- Make sure your Google Sheet has a tab named exactly "Products"
- Check spelling and capitalization
- Create the "Boards" worksheet too

## Product Selection Issues

### "Not enough eligible products"

**Problem**: `RuntimeError: Not enough eligible products`

**Solution**:
1. Add more products to your Google Sheet with Status = READY
2. Or reduce `COOLDOWN_DAYS` in `config.py`
3. Or reduce `MIN_READY_PRODUCTS` in `config.py`
4. Check that products have Priority values (1-5)

### "All products are USED"

**Problem**: No READY products available

**Solution**:
1. Manually change some products back to READY in Google Sheets
2. Or wait for the cooldown period to pass
3. Or reduce `COOLDOWN_DAYS` in `config.py`

## LLM Issues

### "Rate limit exceeded"

**Problem**: `RateLimitError: Rate limit exceeded`

**Solution**:
- Wait a few minutes and try again
- Check your API usage/quota
- Upgrade your API plan if needed
- Increase `API_RETRY_DELAY` in `config.py`

### "Timeout error"

**Problem**: `TimeoutError: Request timed out`

**Solution**:
- Check your internet connection
- Increase `LLM_TIMEOUT` in `config.py`
- Try a different LLM provider

### "Invalid CSV output"

**Problem**: `ValueError: CSV parsing error`

**Solution**:
- Check the logs to see what the LLM returned
- Try a different model (e.g., GPT-4 instead of GPT-3.5)
- Adjust `LLM_TEMPERATURE` (lower = more consistent)
- Check the prompt template in `prompts/ai_prompt_template.txt`

## CSV Validation Issues

### "Missing required disclosure"

**Problem**: `ValueError: DESC missing required disclosure`

**Solution**:
- The LLM didn't include the disclosure text
- Check your prompt template
- Try running again (LLMs can be inconsistent)
- Use a more reliable model

### "Wrong number of rows"

**Problem**: `ValueError: Expected 10 rows, got 8`

**Solution**:
- The LLM didn't generate all rows
- Try running again
- Check the prompt template
- Use a more capable model (e.g., GPT-4, Claude)

## Scheduling Issues

### "Cron job not running"

**Problem**: Script doesn't run automatically

**Solution**:
```bash
# Check cron logs (macOS)
log show --predicate 'process == "cron"' --last 1h

# Check your crontab
crontab -l

# Make sure script is executable
chmod +x run_daily_csv.sh

# Test the script manually
./run_daily_csv.sh
```

### "Task Scheduler not working" (Windows)

**Problem**: Windows Task Scheduler doesn't run the script

**Solution**:
1. Open Task Scheduler
2. Find your task
3. Right-click → "Run" to test
4. Check "History" tab for errors
5. Make sure "Run whether user is logged on or not" is checked
6. Make sure the path to `run_daily_csv.bat` is correct

### "Permission denied" on shell script

**Problem**: `Permission denied: ./run_daily_csv.sh`

**Solution**:
```bash
chmod +x run_daily_csv.sh
chmod +x daily_canva_csv.py
```

## Output Issues

### "CSV file not created"

**Problem**: No file in `daily_csv/` directory

**Solution**:
- Check the logs in `logs/pinterest_automation.log`
- Make sure the script ran without errors
- Check that `OUTPUT_DIR` in `config.py` is correct
- Make sure the directory exists and is writable

### "Can't upload CSV to Canva"

**Problem**: Canva rejects the CSV file

**Solution**:
- Open the CSV in a text editor to check formatting
- Make sure it has the correct header row
- Check for special characters or encoding issues
- Try opening in Excel/Google Sheets first
- Re-save as UTF-8 CSV

## Logging Issues

### "No log file created"

**Problem**: `logs/pinterest_automation.log` doesn't exist

**Solution**:
- Make sure `logs/` directory exists
- Check `LOG_FILE` setting in `config.py`
- Check file permissions on the logs directory

### "Can't read logs"

**Problem**: Log file is empty or unreadable

**Solution**:
```bash
# View recent logs
tail -50 logs/pinterest_automation.log

# View in real-time
tail -f logs/pinterest_automation.log

# Search for errors
grep ERROR logs/pinterest_automation.log
```

## General Debugging

### Enable debug logging

Edit `config.py`:
```python
LOG_LEVEL = "DEBUG"
```

This will show much more detailed information.

### Test each component separately

```python
# Test Google Sheets connection
from src.google_sheets import GoogleSheetsManager
import config
sheets = GoogleSheetsManager(config.GOOGLE_SHEET_ID, config.GOOGLE_CREDENTIALS_FILE)
products = sheets.load_products()
print(f"Loaded {len(products)} products")

# Test LLM
from src.llm_client import LLMClient
client = LLMClient(config.LLM_PROVIDER)
result = client.generate_csv("Test prompt")
print(result)
```

### Check dependencies

```bash
pip list | grep -E "gspread|openai|anthropic|google"
```

### Reinstall everything

```bash
# Remove virtual environment
rm -rf venv

# Recreate it
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Getting Help

If you're still stuck:

1. Check the logs: `logs/pinterest_automation.log`
2. Run with debug logging: `LOG_LEVEL = "DEBUG"`
3. Test the script manually: `python3 daily_canva_csv.py`
4. Check all documentation in `docs/`
5. Review your configuration in `config.py`
6. Make sure all prerequisites are met (see README.md)

## Common Error Messages

| Error | Likely Cause | Solution |
|-------|--------------|----------|
| `ModuleNotFoundError` | Missing dependency | `pip install -r requirements.txt` |
| `FileNotFoundError` | Missing file | Check file paths in config.py |
| `PermissionError` | File permissions | `chmod +x` or check file ownership |
| `AuthenticationError` | Invalid API key | Check API key in config.py |
| `APIError` | Google Sheets issue | Check sharing and permissions |
| `ValueError` | Invalid data | Check logs for details |
| `TimeoutError` | Network/API timeout | Check internet, increase timeout |

