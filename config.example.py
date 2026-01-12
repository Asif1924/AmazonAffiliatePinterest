"""
Configuration file for Amazon Affiliate Pinterest automation.
Copy this file to config.py and fill in your actual values.
"""

# ========== GOOGLE SHEETS CONFIGURATION ==========
# Get your Sheet ID from the URL:
# https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit
GOOGLE_SHEET_ID = "YOUR_GOOGLE_SHEET_ID_HERE"
GOOGLE_WORKSHEET_PRODUCTS = "Products"
GOOGLE_WORKSHEET_BOARDS = "Boards"

# Path to your Google Service Account credentials JSON file
# See README for instructions on creating this
GOOGLE_CREDENTIALS_FILE = "credentials/google_service_account.json"

# ========== LLM CONFIGURATION ==========
# Choose your LLM provider: "openai", "anthropic", "google", or "openrouter"
LLM_PROVIDER = "openai"

# API Keys (only fill in the one you're using)
OPENAI_API_KEY = "sk-..."
ANTHROPIC_API_KEY = "sk-ant-..."
GOOGLE_API_KEY = "..."
OPENROUTER_API_KEY = "sk-or-..."

# Model names for each provider
OPENAI_MODEL = "gpt-4o"  # or "gpt-4o-mini", "gpt-4-turbo"
ANTHROPIC_MODEL = "claude-3-5-sonnet-20241022"  # or "claude-3-opus-20240229"
GOOGLE_MODEL = "gemini-pro"
OPENROUTER_MODEL = "anthropic/claude-3.5-sonnet"  # or any OpenRouter model

# ========== PRODUCT SELECTION CONFIGURATION ==========
# Number of products to generate per day
DAILY_COUNT = 10

# Don't reuse the same product within this many days
COOLDOWN_DAYS = 14

# Minimum number of READY products required to run
MIN_READY_PRODUCTS = 20

# ========== OUTPUT CONFIGURATION ==========
# Directory where daily CSV files will be saved
OUTPUT_DIR = "./daily_csv"

# CSV filename pattern (date will be inserted)
CSV_FILENAME_PATTERN = "canva_bulk_{date}.csv"

# ========== LOGGING CONFIGURATION ==========
# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = "INFO"

# Log file path (set to None to disable file logging)
LOG_FILE = "./logs/pinterest_automation.log"

# ========== ADVANCED SETTINGS ==========
# Temperature for LLM (0.0 = deterministic, 1.0 = creative)
LLM_TEMPERATURE = 0.7

# Maximum tokens for LLM response
# Increased to 6000 to accommodate 10 products with long Amazon URLs
LLM_MAX_TOKENS = 6000

# Timeout for LLM API calls (seconds)
LLM_TIMEOUT = 60

# Retry attempts for failed API calls
API_RETRY_ATTEMPTS = 3

# Delay between retries (seconds)
API_RETRY_DELAY = 2

# ========== VALIDATION SETTINGS ==========
# Required columns in output CSV
REQUIRED_CSV_COLUMNS = ["HOOK", "TITLE", "SUBTITLE", "DESC", "URL", "FILENAME", "BOARD"]

# Required disclosure text in descriptions
REQUIRED_DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."

# Minimum length for HOOK (words)
MIN_HOOK_WORDS = 3

# Maximum length for HOOK (words)
MAX_HOOK_WORDS = 7

# Minimum length for TITLE (characters)
MIN_TITLE_LENGTH = 40

# Maximum length for TITLE (characters)
MAX_TITLE_LENGTH = 70

# ========== SCHEDULING CONFIGURATION ==========
# Preferred time to run (24-hour format, for documentation purposes)
PREFERRED_RUN_TIME = "09:00"

# Timezone for scheduling
TIMEZONE = "America/New_York"  # Change to your timezone

