# Implementation Checklist

Use this checklist to set up your Amazon Affiliate Pinterest automation system.

## ✅ Phase 1: Initial Setup (30 minutes)

### Python Environment
- [ ] Python 3.8+ installed
- [ ] Run `./setup.sh` (or manually create venv and install requirements)
- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list` shows gspread, openai, etc.)

### Project Files
- [ ] All files downloaded/cloned
- [ ] `config.example.py` copied to `config.py`
- [ ] `.gitignore` in place
- [ ] Directories created: `credentials/`, `daily_csv/`, `logs/`

## ✅ Phase 2: Google Sheets Setup (15 minutes)

### Create Google Sheet
- [ ] New Google Sheet created
- [ ] Named: "Amazon Affiliate Pinterest Products" (or your choice)
- [ ] Sheet ID copied from URL

### Products Worksheet
- [ ] Worksheet named "Products" created
- [ ] Column headers A-W added (see docs/GOOGLE_SHEETS_SETUP.md)
- [ ] Formula in S2 (PinTitle) added and copied down
- [ ] Formula in T2 (PinHookOverlay) added and copied down
- [ ] Formula in U2 (PinDescription) added and copied down
- [ ] Formula in V2 (BoardName) added and copied down
- [ ] Formula in W2 (CanvaImageName) added and copied down

### Boards Worksheet
- [ ] Worksheet named "Boards" created
- [ ] Headers: Niche (A), BoardName (B)
- [ ] 6 niche mappings added (electronics, home/kitchen, tools, fitness, cars, computer accessories)

### Sample Products
- [ ] At least 10 sample products added
- [ ] All required fields filled in
- [ ] Status set to "READY"
- [ ] Priority values assigned (1-5)
- [ ] Formulas auto-populated columns S-W

## ✅ Phase 3: Google API Setup (10 minutes)

### Google Cloud Console
- [ ] Visited [Google Cloud Console](https://console.cloud.google.com/)
- [ ] New project created (or existing selected)
- [ ] "Google Sheets API" enabled
- [ ] "Google Drive API" enabled

### Service Account
- [ ] Service Account created
- [ ] Service Account name set (e.g., "pinterest-automation")
- [ ] JSON key downloaded
- [ ] JSON saved as `credentials/google_service_account.json`
- [ ] Service account email copied (from JSON file)

### Sheet Sharing
- [ ] Google Sheet shared with service account email
- [ ] Permission set to "Editor"
- [ ] Share invitation sent

## ✅ Phase 4: LLM API Setup (5 minutes)

### Choose Provider
- [ ] LLM provider chosen (OpenAI, Anthropic, Google, or OpenRouter)
- [ ] Account created with chosen provider
- [ ] API key generated
- [ ] API key copied

### Test API Access
- [ ] API key has available credits/quota
- [ ] API key tested (optional: use provider's playground)

## ✅ Phase 5: Configuration (5 minutes)

### Edit config.py
- [ ] `GOOGLE_SHEET_ID` set (from Sheet URL)
- [ ] `GOOGLE_CREDENTIALS_FILE` path verified
- [ ] `LLM_PROVIDER` set (openai/anthropic/google/openrouter)
- [ ] Appropriate API key set (OPENAI_API_KEY, etc.)
- [ ] `DAILY_COUNT` set (default: 10)
- [ ] `COOLDOWN_DAYS` set (default: 14)
- [ ] `OUTPUT_DIR` set (default: ./daily_csv)
- [ ] `LOG_LEVEL` set (default: INFO)

### Verify Configuration
- [ ] No syntax errors in config.py
- [ ] All required settings filled in
- [ ] Paths are correct

## ✅ Phase 6: Testing (10 minutes)

### First Test Run
- [ ] Run: `python3 daily_canva_csv.py`
- [ ] Script connects to Google Sheets successfully
- [ ] Products loaded (check log output)
- [ ] 10 products selected
- [ ] LLM called successfully
- [ ] CSV validated
- [ ] CSV file created in `daily_csv/`
- [ ] Google Sheet updated (10 products marked USED)
- [ ] No errors in logs

### Verify Output
- [ ] CSV file exists: `daily_csv/canva_bulk_YYYY-MM-DD.csv`
- [ ] CSV has header row
- [ ] CSV has 10 data rows
- [ ] All required columns present (HOOK, TITLE, SUBTITLE, DESC, URL, FILENAME, BOARD)
- [ ] Disclosure text present in DESC column
- [ ] URLs are valid Amazon affiliate links

### Check Google Sheet
- [ ] 10 products now have Status = "USED"
- [ ] LastUsedDate updated to today
- [ ] Formulas still working in columns S-W

## ✅ Phase 7: Canva Setup (15 minutes)

### Create Templates
- [ ] Canva account created/logged in
- [ ] Template T1 created (1000 x 1500 px)
- [ ] Placeholder `{{HOOK}}` added to T1
- [ ] Placeholder `{{TITLE}}` added to T1
- [ ] Placeholder `{{SUBTITLE}}` added to T1
- [ ] Placeholder `{{DESC}}` added to T1 (optional)
- [ ] T1 saved with clear name
- [ ] Templates T2-T5 created with different styles
- [ ] All templates saved

### Test Bulk Create
- [ ] Opened template T1 in Canva
- [ ] Clicked "Apps" → "Bulk Create"
- [ ] Uploaded today's CSV file
- [ ] Data mapped correctly to placeholders
- [ ] Generated 10 pins
- [ ] Reviewed all pins for quality
- [ ] Downloaded pins as PNG files
- [ ] Filenames match CSV FILENAME column

## ✅ Phase 8: Automation (Optional, 10 minutes)

### macOS/Linux
- [ ] `run_daily_csv.sh` is executable (`chmod +x`)
- [ ] Edited paths in `run_daily_csv.sh`
- [ ] Tested: `./run_daily_csv.sh`
- [ ] Crontab edited: `crontab -e`
- [ ] Cron job added (e.g., `0 9 * * *`)
- [ ] Cron job verified: `crontab -l`

### Windows
- [ ] `run_daily_csv.bat` edited with correct paths
- [ ] Tested: `run_daily_csv.bat`
- [ ] Task Scheduler opened
- [ ] New task created
- [ ] Trigger set (daily at chosen time)
- [ ] Action set (run batch file)
- [ ] Task tested manually

### Verify Automation
- [ ] Script runs without user interaction
- [ ] Logs are created
- [ ] CSV files are generated
- [ ] Google Sheet is updated

## ✅ Phase 9: Pinterest Setup (Outside this project)

### Pinterest Account
- [ ] Pinterest business account created
- [ ] Boards created matching your niche mappings
- [ ] Profile optimized
- [ ] Amazon affiliate disclosure in profile

### Posting Strategy
- [ ] Posting schedule planned
- [ ] Pin descriptions prepared
- [ ] Hashtag strategy defined
- [ ] Analytics tracking set up

## ✅ Phase 10: Ongoing Maintenance

### Weekly
- [ ] Check logs for errors
- [ ] Verify CSV generation
- [ ] Monitor Pinterest performance

### Monthly
- [ ] Add 10-20 new products to Google Sheet
- [ ] Review product performance
- [ ] Adjust priorities based on results
- [ ] Update Canva templates if needed

### Quarterly
- [ ] Review overall system performance
- [ ] Update top-performing products
- [ ] Refresh product selection
- [ ] Optimize copy based on learnings

## 🎉 Completion

When all items are checked:
- ✅ System is fully operational
- ✅ Daily automation is running
- ✅ Pins are being generated
- ✅ Ready to scale up!

## 📚 Resources

- **Quick Start**: `QUICK_START.md`
- **Full Documentation**: `README.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING.md`
- **Google Sheets**: `docs/GOOGLE_SHEETS_SETUP.md`
- **Canva**: `docs/CANVA_TEMPLATE_SETUP.md`
- **Scheduling**: `docs/SCHEDULING.md`

## 🆘 Need Help?

If you get stuck:
1. Check `logs/pinterest_automation.log`
2. See `docs/TROUBLESHOOTING.md`
3. Review the relevant documentation
4. Set `LOG_LEVEL = "DEBUG"` for more details

---

**Happy automating! 🚀**

