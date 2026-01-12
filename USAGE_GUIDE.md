# Daily Canva CSV Generator - Usage Guide

## Quick Start

### Running the Script

```bash
python3 daily_canva_csv.py
```

The script will:
1. ✅ Connect to Google Sheets
2. ✅ Select 10 eligible products (not used today)
3. ✅ Generate Pinterest-optimized copy using AI
4. ✅ Create a CSV file in `daily_csv/canva_bulk_YYYY-MM-DD.csv`
5. ✅ Mark products as USED in Google Sheets

### Expected Output

```
2026-01-11 23:24:56 - INFO - SUCCESS! CSV generated and products updated
2026-01-11 23:24:56 - INFO - Output file: daily_csv/canva_bulk_2026-01-11.csv
```

## CSV File Format

The generated CSV has these columns:

| Column | Description | Example |
|--------|-------------|---------|
| HOOK | Attention-grabbing question/statement | "Cook like a chef" |
| TITLE | Product title (40-70 chars recommended) | "Lodge Cast Iron Skillet: Pro Cooking" |
| SUBTITLE | Short benefit statement | "Perfect for home and camp" |
| DESC | Full description with keywords & disclosure | "Master every meal with... As an Amazon Associate I earn from qualifying purchases. #ad" |
| URL | Amazon affiliate link | https://www.amazon.ca/... |
| FILENAME | Image filename for Canva | 2026-01-11_T1_PROD026.png |
| BOARD | Pinterest board name | "Kitchen Upgrades & Must-Haves" |

## Using the CSV in Canva

1. **Open Canva Bulk Create**
   - Go to Canva.com
   - Create or open your Pinterest pin template
   - Click "Apps" → "Bulk Create"

2. **Upload CSV**
   - Click "Upload CSV"
   - Select `daily_csv/canva_bulk_2026-01-11.csv`
   - Map columns to your template fields

3. **Generate Pins**
   - Review the preview
   - Click "Generate" to create all 10 pins
   - Download as PNG files

## Configuration

### Key Settings in `config.py`

```python
# Number of products to generate daily
DAILY_COUNT = 10

# LLM provider (openai or anthropic)
LLM_PROVIDER = "openai"

# Maximum tokens for LLM response
LLM_MAX_TOKENS = 6000  # Enough for 10 products with long URLs

# Log level (INFO for normal, DEBUG for troubleshooting)
LOG_LEVEL = "INFO"
```

### Google Sheets Setup

Your Google Sheet should have these columns:
- `ProductID` - Unique identifier (e.g., PROD001)
- `ProductName` - Product name
- `AmazonURL` - Affiliate link
- `Category` - Product category
- `Priority` - 1-5 (higher = more important)
- `LastUsed` - Date last used (YYYY-MM-DD)
- `Board` - Pinterest board name

## Product Selection Logic

The script selects products based on:

1. **Not used today** - `LastUsed` is not today's date
2. **Priority** - Higher priority products selected first
3. **Randomization** - Within same priority, random selection
4. **Limit** - Exactly `DAILY_COUNT` products (default: 10)

## Troubleshooting

### Error: "Missing required columns"

**Cause:** LLM didn't generate proper CSV format

**Solution:** 
1. Check `LLM_MAX_TOKENS` is set to 6000
2. Review `prompts/ai_prompt_template.txt`
3. Set `LOG_LEVEL = "DEBUG"` to see full LLM response

### Error: "Expected 10 rows, got X"

**Cause:** LLM response was truncated

**Solution:** Increase `LLM_MAX_TOKENS` in `config.py`

### Warning: "TITLE has X chars (recommended: 40-70)"

**Cause:** Title is too short or too long

**Impact:** This is just a warning. The CSV will still be generated.

**Solution:** Adjust the prompt template to encourage longer/shorter titles

### Error: "No eligible products found"

**Cause:** All products were used today

**Solution:** 
1. Wait until tomorrow, OR
2. Manually clear `LastUsed` dates in Google Sheets, OR
3. Add more products to your sheet

## File Structure

```
AmazonAffiliatePinterest/
├── daily_canva_csv.py          # Main script
├── config.py                    # Your configuration
├── config.example.py            # Template configuration
├── prompts/
│   └── ai_prompt_template.txt  # AI prompt template
├── src/
│   ├── csv_validator.py        # CSV validation logic
│   ├── llm_client.py           # LLM API client
│   ├── product_selector.py     # Product selection logic
│   └── sheets_client.py        # Google Sheets integration
└── daily_csv/
    └── canva_bulk_2026-01-11.csv  # Generated CSV files
```

## Best Practices

### 1. Run Daily
Set up a cron job or scheduled task to run the script daily:

```bash
# Run at 8 AM every day
0 8 * * * cd /path/to/AmazonAffiliatePinterest && python3 daily_canva_csv.py
```

### 2. Review Output
Occasionally review the generated CSV to ensure quality:

```bash
cat daily_csv/canva_bulk_$(date +%Y-%m-%d).csv
```

### 3. Monitor Costs
If using OpenAI API, monitor your usage:
- Each run uses approximately 3,000-4,000 tokens
- At $0.01 per 1K tokens, that's about $0.03-$0.04 per run
- Monthly cost: ~$1-$2 for daily runs

### 4. Backup Google Sheets
Regularly backup your Google Sheet to avoid data loss.

### 5. Update Products
Keep your product list fresh:
- Add new products regularly
- Update priorities based on performance
- Remove discontinued products

## Advanced Usage

### Custom Prompt Template

Edit `prompts/ai_prompt_template.txt` to customize:
- Writing style
- Keyword density
- Hook patterns
- Description length

### Multiple Boards

The script automatically assigns products to boards based on the `Board` column in Google Sheets.

### Batch Processing

To generate multiple days at once:

```bash
for i in {1..7}; do
    python3 daily_canva_csv.py
    sleep 60  # Wait 1 minute between runs
done
```

## Support

For issues or questions:
1. Check `FIX_SUMMARY.md` for common problems
2. Set `LOG_LEVEL = "DEBUG"` for detailed logs
3. Review the error message and stack trace

## Version History

- **v1.1** (2026-01-11) - Fixed CSV header and max_tokens issues
- **v1.0** (2026-01-10) - Initial release

