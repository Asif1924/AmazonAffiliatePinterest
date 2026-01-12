# Quick Start Guide

Get up and running in 30 minutes!

## Prerequisites

- Python 3.8 or higher
- Google account
- Amazon Associate account
- Canva account (free or pro)
- API key for an LLM provider (OpenAI, Anthropic, Google, or OpenRouter)

## Step-by-Step Setup

### 1. Install Dependencies (5 minutes)

```bash
# Run the setup script
./setup.sh

# Or manually:
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Up Google Sheets (10 minutes)

1. Create a new Google Sheet
2. Create two worksheets: "Products" and "Boards"
3. Copy the column headers from `docs/GOOGLE_SHEETS_SETUP.md`
4. Add the formulas to columns S, T, U, V, W
5. Fill in the Boards worksheet with niche mappings
6. Add at least 10 sample products (see `docs/EXAMPLE_PRODUCTS.md`)

### 3. Enable Google Sheets API (5 minutes)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable "Google Sheets API" and "Google Drive API"
4. Create a Service Account
5. Download the JSON key file
6. Save it as `credentials/google_service_account.json`
7. Share your Google Sheet with the service account email

### 4. Configure the Script (5 minutes)

```bash
# Copy the example config
cp config.example.py config.py

# Edit config.py
nano config.py  # or use your preferred editor
```

**Required settings:**
- `GOOGLE_SHEET_ID` - From your Google Sheet URL
- `LLM_PROVIDER` - Choose: "openai", "anthropic", "google", or "openrouter"
- API key for your chosen provider (e.g., `OPENAI_API_KEY`)

### 5. Test the Script (2 minutes)

```bash
python3 daily_canva_csv.py
```

**Expected output:**
- ✅ Connects to Google Sheets
- ✅ Loads products
- ✅ Selects 10 products
- ✅ Calls LLM
- ✅ Validates CSV
- ✅ Saves to `daily_csv/canva_bulk_YYYY-MM-DD.csv`
- ✅ Updates Google Sheet

### 6. Set Up Canva Templates (5 minutes)

1. Go to Canva
2. Create a Pinterest Pin (1000 x 1500 px)
3. Add text placeholders by clicking on "Text" in the left sidebar, then add text boxes and type:
   - `{{HOOK}}` - Main attention-grabbing headline (large, bold text at top)
   - `{{TITLE}}` - Product title or secondary headline
   - `{{SUBTITLE}}` - Supporting text or benefit statement
   - `{{DESC}}` - Additional description or call-to-action
4. Design 5 templates (T1-T5) with different styles
5. Save each template: Click the "Share" button (top right) → "Template link" → "Create template" (or simply save the design and use it directly for Bulk Create)

### 7. Generate Your First Pins (3 minutes)

1. Open one of your Canva templates
2. Click "Apps" → "Bulk Create"
3. Upload the CSV file from `daily_csv/`
4. Review the generated pins
5. Download all as PNG files

### 8. Schedule Daily Execution (Optional)

**macOS/Linux:**
```bash
crontab -e
# Add: 0 9 * * * /path/to/run_daily_csv.sh
```

**Windows:**
- Use Task Scheduler to run `run_daily_csv.bat` daily

See `docs/SCHEDULING.md` for detailed instructions.

## Daily Workflow

Once set up, your daily workflow is:

1. **Script runs automatically** (or run manually: `python3 daily_canva_csv.py`)
2. **Check the CSV** in `daily_csv/` folder
3. **Upload to Canva** Bulk Create
4. **Generate pins** in Canva
5. **Download** the pins
6. **Upload to Pinterest** with scheduling

That's it! 🎉

## Troubleshooting

If something goes wrong:

1. Check `logs/pinterest_automation.log`
2. See `docs/TROUBLESHOOTING.md`
3. Run with debug logging: Set `LOG_LEVEL = "DEBUG"` in `config.py`

## Next Steps

- Add more products to your Google Sheet (aim for 30+)
- Experiment with different angles and hook styles
- Track which products perform best on Pinterest
- Adjust priorities based on performance
- Create more Canva templates for variety

## Tips for Success

✅ **Start small** - Test with 10 products first  
✅ **Use real products** - Only promote products you'd actually recommend  
✅ **Be compliant** - Always include disclosure text  
✅ **Track performance** - Note which products get clicks  
✅ **Refresh regularly** - Add new products monthly  
✅ **Vary your content** - Use different angles and templates  
✅ **Schedule pins** - Use Pinterest's scheduler for consistent posting  

## Resources

- **Full Documentation**: `README.md`
- **Google Sheets Setup**: `docs/GOOGLE_SHEETS_SETUP.md`
- **Canva Templates**: `docs/CANVA_TEMPLATE_SETUP.md`
- **Scheduling**: `docs/SCHEDULING.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING.md`
- **Example Products**: `docs/EXAMPLE_PRODUCTS.md`

## Support

Need help? Check:
1. The documentation in `docs/`
2. The troubleshooting guide
3. The logs in `logs/`
4. The example products for reference

Happy pinning! 📌

