# Amazon Affiliate Pinterest Automation

Automated system for generating Pinterest pins for Amazon affiliate products using AI and Canva Bulk Create.

## 🎯 What This Does

1. **Stores products** in Google Sheets with all metadata
2. **Selects 10 products daily** using smart priority-based selection
3. **Generates Pinterest copy** using AI (OpenAI, Anthropic, Google, or OpenRouter)
4. **Creates Canva CSV** for bulk pin generation
5. **Tracks usage** to avoid repeating products too soon
6. **Fully automated** - runs daily on schedule

## 📋 Features

- ✅ Google Sheets integration for product management
- ✅ Multiple LLM provider support (OpenAI, Anthropic, Google, OpenRouter)
- ✅ Smart product selection with priority weighting
- ✅ Cooldown period to avoid repetition
- ✅ FTC-compliant disclosure text
- ✅ CSV validation and error handling
- ✅ Comprehensive logging
- ✅ Easy scheduling (cron, Task Scheduler, launchd)

## 🚀 Quick Start

### 1. Clone and Install

```bash
cd /path/to/your/projects
git clone <your-repo-url> AmazonAffiliatePinterest
cd AmazonAffiliatePinterest

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Set Up Google Sheets

Follow the detailed guide: [docs/GOOGLE_SHEETS_SETUP.md](docs/GOOGLE_SHEETS_SETUP.md)

**Quick summary:**
1. Create a Google Sheet with "Products" and "Boards" worksheets
2. Add column headers and formulas
3. Fill in at least 20-30 products
4. Get your Sheet ID from the URL

### 3. Enable Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable "Google Sheets API" and "Google Drive API"
4. Create a Service Account:
   - Go to "IAM & Admin" → "Service Accounts"
   - Click "Create Service Account"
   - Name it (e.g., "pinterest-automation")
   - Click "Create and Continue"
   - Skip optional steps
5. Create a key:
   - Click on the service account
   - Go to "Keys" tab
   - Click "Add Key" → "Create new key"
   - Choose JSON format
   - Download the file
6. Save the JSON file as `credentials/google_service_account.json`
7. Share your Google Sheet with the service account email (found in the JSON file)

### 4. Configure the Script

```bash
# Copy example config
cp config.example.py config.py

# Edit config.py with your settings
nano config.py  # or use your preferred editor
```

**Required settings:**
- `GOOGLE_SHEET_ID` - Your Google Sheet ID
- `LLM_PROVIDER` - Choose: "openai", "anthropic", "google", or "openrouter"
- API key for your chosen provider

### 5. Test the Script

```bash
python3 daily_canva_csv.py
```

If successful, you'll see:
- A CSV file in `daily_csv/canva_bulk_YYYY-MM-DD.csv`
- 10 products marked as "USED" in your Google Sheet
- Logs in `logs/pinterest_automation.log`

### 6. Set Up Canva Templates

Follow the guide: [docs/CANVA_TEMPLATE_SETUP.md](docs/CANVA_TEMPLATE_SETUP.md)

Create 5 Pinterest pin templates (T1-T5) with placeholders:
- `{{HOOK}}`
- `{{TITLE}}`
- `{{SUBTITLE}}`
- `{{DESC}}`
- `{{URL}}`

### 7. Schedule Daily Execution

Follow the guide: [docs/SCHEDULING.md](docs/SCHEDULING.md)

**macOS/Linux (cron):**
```bash
crontab -e
# Add: 0 9 * * * /path/to/run_daily_csv.sh
```

**Windows (Task Scheduler):**
- Create a task to run `run_daily_csv.bat` daily

## 📁 Project Structure

```
AmazonAffiliatePinterest/
├── daily_canva_csv.py          # Main script
├── config.example.py            # Configuration template
├── config.py                    # Your config (gitignored)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── src/                         # Source modules
│   ├── __init__.py
│   ├── google_sheets.py         # Google Sheets integration
│   ├── llm_client.py            # LLM API client
│   ├── product_selector.py     # Product selection logic
│   ├── csv_validator.py        # CSV validation
│   └── logger.py                # Logging setup
│
├── docs/                        # Documentation
│   ├── GOOGLE_SHEETS_SETUP.md
│   ├── CANVA_TEMPLATE_SETUP.md
│   └── SCHEDULING.md
│
├── prompts/                     # AI prompts
│   └── ai_prompt_template.txt
│
├── credentials/                 # API credentials (gitignored)
│   └── google_service_account.json
│
├── daily_csv/                   # Generated CSV files
│   └── canva_bulk_YYYY-MM-DD.csv
│
└── logs/                        # Log files
    └── pinterest_automation.log
```

## 🔧 Configuration Options

See `config.example.py` for all available options:

- **Product Selection**: `DAILY_COUNT`, `COOLDOWN_DAYS`, `MIN_READY_PRODUCTS`
- **LLM Settings**: Provider, model, temperature, max tokens
- **Output**: Directory, filename pattern
- **Logging**: Level, file path
- **Validation**: Required columns, disclosure text

## 📊 Daily Workflow

1. **Script runs** (scheduled or manual)
2. **Connects** to Google Sheets
3. **Loads** all products
4. **Filters** READY products not in cooldown
5. **Selects** 10 products (priority-weighted)
6. **Calls** LLM with product data
7. **Validates** CSV output
8. **Saves** CSV file
9. **Updates** Google Sheet (marks products as USED)
10. **You upload** CSV to Canva Bulk Create
11. **Generate** 10 pins in Canva
12. **Download** and post to Pinterest

## 🎨 Using with Canva

1. Open your Canva template (T1-T5)
2. Click "Apps" → "Bulk Create"
3. Upload today's CSV file
4. Review generated pins
5. Download all as PNG
6. Upload to Pinterest with scheduling

## 🐛 Troubleshooting

### "config.py not found"
```bash
cp config.example.py config.py
# Then edit config.py
```

### "Credentials file not found"
- Make sure `credentials/google_service_account.json` exists
- Check the path in `config.py`

### "Not enough eligible products"
- Add more products to Google Sheets with Status = READY
- Or reduce `COOLDOWN_DAYS` in config.py

### "Failed to connect to Google Sheets"
- Check your service account JSON file
- Make sure you shared the Sheet with the service account email
- Verify Sheet ID in config.py

### "LLM API error"
- Check your API key in config.py
- Verify you have API credits/quota
- Check internet connection

## 📝 Best Practices

1. **Start with 30+ products** - Ensures variety and avoids running out
2. **Use priority wisely** - Set 5 for best performers, 1 for testing
3. **Monitor logs** - Check weekly to ensure smooth operation
4. **Test before scheduling** - Always run manually first
5. **Backup your Sheet** - Export regularly
6. **Track performance** - Note which products/angles work best
7. **Refresh products** - Add new ones monthly

## 🔒 Security

- ✅ `config.py` is gitignored (contains API keys)
- ✅ `credentials/` is gitignored (contains service account key)
- ✅ Never commit sensitive data
- ✅ Use environment variables for production

## 📄 License

MIT License - feel free to use and modify

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Support

For issues or questions:
1. Check the documentation in `docs/`
2. Review logs in `logs/`
3. Open an issue on GitHub

## 🎉 Credits

Built following the outline from `Outline.txt` - a comprehensive system for Pinterest affiliate marketing automation.

---

**Happy pinning! 📌**

