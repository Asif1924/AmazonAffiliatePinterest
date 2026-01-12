# Fix Summary - daily_canva_csv.py Error Resolution

## Problem

When running `daily_canva_csv.py`, you encountered this error:

```
ValueError: Failed to parse CSV: Missing required columns: BOARD, DESC, FILENAME, HOOK, SUBTITLE, TITLE, URL
```

## Root Causes

The error was caused by **two issues** with the LLM (GPT-4) response:

### 1. Missing CSV Header Row
The LLM was returning CSV data **without the header row**. The CSV parser was treating the first data row as the header, which caused the column names to be the actual data values instead of "HOOK", "TITLE", etc.

### 2. Truncated Response (Insufficient max_tokens)
The `LLM_MAX_TOKENS` setting was set to 2000, which was **too low** to generate all 10 products with long Amazon affiliate URLs. The response was being cut off after 5-9 rows instead of the required 10 rows.

### 3. Missing Field Quoting
The LLM wasn't quoting CSV fields, which caused parsing errors when fields contained commas (like the DESC field with keywords).

## Solutions Applied

### Fix 1: Updated AI Prompt Template
**File:** `prompts/ai_prompt_template.txt`

**Changes:**
- Made CSV formatting rules more explicit and prominent
- Added "CRITICAL CSV FORMATTING RULES" section
- Emphasized that ALL fields must be enclosed in double quotes
- Made header row requirement more explicit with "IMPORTANT" note

**Before:**
```
Output must be valid CSV, comma-separated, UTF-8, with a header row and exactly 10 data rows.
Quote fields with double quotes and escape inner quotes by doubling them.
...
Header: HOOK,TITLE,SUBTITLE,DESC,URL,FILENAME,BOARD
Then 10 rows, in the same order as inputs.
```

**After:**
```
CRITICAL CSV FORMATTING RULES:
- ALL fields MUST be enclosed in double quotes ("field content")
- If a field contains a double quote, escape it by doubling it ("")
...
Output MUST start with this exact header line:
HOOK,TITLE,SUBTITLE,DESC,URL,FILENAME,BOARD

Then output exactly 10 data rows, in the same order as inputs.

IMPORTANT: The first line of your output MUST be the header row shown above.
```

### Fix 2: Increased max_tokens
**Files:** `config.py` and `config.example.py`

**Change:**
```python
# Before
LLM_MAX_TOKENS = 2000

# After
LLM_MAX_TOKENS = 6000  # Increased to accommodate 10 products with long Amazon URLs
```

**Reason:** Amazon affiliate URLs are very long (often 500-800 characters each). With 10 products, the total response needs approximately 10,000-11,000 characters, which requires about 3,000-4,000 tokens. Setting it to 6000 provides a comfortable buffer.

### Fix 3: Improved Error Messages
**File:** `src/csv_validator.py`

**Change:** Added CSV preview to error messages to help debug future issues:
```python
raise ValueError(
    f"Missing required columns: {', '.join(sorted(missing))}. "
    f"Found columns: {', '.join(header)}\n\n"
    f"CSV Preview:\n{csv_preview}"
)
```

### Fix 4: Enhanced Debug Logging
**File:** `daily_canva_csv.py`

**Change:** Added full CSV response logging for debugging:
```python
logger.debug("="*60)
logger.debug("Raw LLM CSV response (full):")
logger.debug("="*60)
logger.debug(csv_text)
logger.debug("="*60)
logger.debug(f"Response length: {len(csv_text)} characters")
```

## Verification

After applying these fixes, the script now:

✅ Generates proper CSV with header row  
✅ Includes all 10 products (not truncated)  
✅ Properly quotes all fields  
✅ Includes required disclosure text  
✅ Saves to `daily_csv/canva_bulk_YYYY-MM-DD.csv`  
✅ Updates Google Sheets with USED status  

## Test Results

```
2026-01-11 23:23:18 - INFO - CSV validation passed: 10 rows
2026-01-11 23:23:18 - INFO - CSV saved to daily_csv/canva_bulk_2026-01-11.csv
2026-01-11 23:23:19 - INFO - Marked 10 products as USED
2026-01-11 23:23:19 - INFO - SUCCESS! CSV generated and products updated
```

## Files Modified

1. `prompts/ai_prompt_template.txt` - Improved CSV formatting instructions
2. `config.py` - Increased LLM_MAX_TOKENS from 2000 to 6000
3. `config.example.py` - Updated default LLM_MAX_TOKENS
4. `src/csv_validator.py` - Added CSV preview to error messages
5. `daily_canva_csv.py` - Enhanced debug logging

## Future Recommendations

1. **Monitor token usage**: If you add more products or longer URLs, you may need to increase `LLM_MAX_TOKENS` further.

2. **Check CSV output**: Occasionally review the generated CSV files to ensure quality.

3. **Log level**: Keep `LOG_LEVEL = "INFO"` for normal operation. Change to `"DEBUG"` if you need to troubleshoot.

4. **Cost optimization**: If using OpenAI API, monitor costs. 6000 max_tokens per run may increase costs slightly, but ensures reliability.

## Status

✅ **RESOLVED** - The script now works correctly and generates valid CSV files for Canva Bulk Create.

