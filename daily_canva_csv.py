#!/usr/bin/env python3
"""
daily_canva_csv.py

Generates a Canva Bulk Create CSV with 10 products/day for Pinterest.
- Reads product rows from Google Sheets
- Uses an LLM to generate HOOK/TITLE/SUBTITLE/DESC
- Writes a validated CSV for Canva
- Marks used products in the sheet
"""

import csv
import datetime as dt
import logging
import os
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional

# Import configuration
try:
    import config
except ImportError:
    print("ERROR: config.py not found. Please copy config.example.py to config.py and configure it.")
    sys.exit(1)

# Import modules
from src.google_sheets import GoogleSheetsManager
from src.llm_client import LLMClient
from src.product_selector import ProductSelector
from src.csv_validator import CSVValidator
from src.logger import setup_logger

# Setup logging
logger = setup_logger(__name__, config.LOG_LEVEL, config.LOG_FILE)


@dataclass
class Product:
    """Product data model"""
    product_id: str
    niche: str
    name: str
    brand: str
    key_benefit: str
    features: str
    ideal_for: str
    keywords: str
    price_band: str
    affiliate_url: str
    disclosure: str
    angle: str
    hook_style: str
    template_id: str
    background_theme: str
    status: str
    last_used_date: str
    priority: int
    board: str
    filename: str
    row_number: int  # Track row number for updates


def load_prompt_template() -> str:
    """Load the AI prompt template"""
    prompt_path = Path("prompts/ai_prompt_template.txt")
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt template not found at {prompt_path}")
    
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def build_llm_prompt(selected: List[Product], template: str) -> str:
    """Build the complete LLM prompt with product data"""
    product_lines = []
    for p in selected:
        line = (
            f"{p.name} | {p.niche} | {p.key_benefit} | {p.features} | "
            f"{p.ideal_for} | {p.keywords} | {p.template_id} | {p.board} | "
            f"{p.affiliate_url} | {p.filename}"
        )
        product_lines.append(line)
    
    # Replace placeholder with actual products
    prompt = template.replace("<<INPUT_PRODUCTS>>", "\n".join(product_lines))
    return prompt


def save_csv_file(rows: List[Dict[str, str]], filepath: str) -> None:
    """Save CSV file with proper formatting"""
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=config.REQUIRED_CSV_COLUMNS,
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        writer.writerows(rows)
    logger.info(f"CSV saved to {filepath}")


def main():
    """Main execution function"""
    try:
        logger.info("=" * 60)
        logger.info("Starting Pinterest Canva CSV Generation")
        logger.info("=" * 60)
        
        # Create output directory if it doesn't exist
        output_dir = Path(config.OUTPUT_DIR)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize Google Sheets manager
        logger.info("Connecting to Google Sheets...")
        sheets_manager = GoogleSheetsManager(
            config.GOOGLE_SHEET_ID,
            config.GOOGLE_CREDENTIALS_FILE
        )
        
        # Load products from Google Sheets
        logger.info("Loading products from Google Sheets...")
        products = sheets_manager.load_products()
        logger.info(f"Loaded {len(products)} total products")
        
        # Select eligible products
        logger.info("Selecting eligible products...")
        selector = ProductSelector(config.COOLDOWN_DAYS, config.MIN_READY_PRODUCTS)
        selected = selector.select_products(products, config.DAILY_COUNT)
        logger.info(f"Selected {len(selected)} products for today")
        
        # Log selected products
        for i, p in enumerate(selected, 1):
            logger.info(f"  {i}. {p.product_id}: {p.name} (Priority: {p.priority})")
        
        # Load prompt template
        logger.info("Loading AI prompt template...")
        prompt_template = load_prompt_template()
        
        # Build complete prompt
        logger.info("Building LLM prompt...")
        prompt = build_llm_prompt(selected, prompt_template)
        
        # Call LLM
        logger.info(f"Calling LLM ({config.LLM_PROVIDER})...")
        llm_client = LLMClient(config.LLM_PROVIDER)
        csv_text = llm_client.generate_csv(prompt)

        # Debug: Log the raw CSV response
        logger.debug("Raw LLM CSV response:")
        logger.debug(csv_text[:500] + "..." if len(csv_text) > 500 else csv_text)

        # Validate CSV
        logger.info("Validating CSV output...")
        validator = CSVValidator(config.REQUIRED_CSV_COLUMNS, config.REQUIRED_DISCLOSURE)
        validated_rows = validator.validate(csv_text, config.DAILY_COUNT)
        logger.info(f"CSV validation passed: {len(validated_rows)} rows")
        
        # Save CSV file
        today = dt.date.today().isoformat()
        filename = config.CSV_FILENAME_PATTERN.format(date=today)
        filepath = output_dir / filename
        save_csv_file(validated_rows, str(filepath))
        
        # Update Google Sheets
        logger.info("Updating Google Sheets...")
        product_ids = [p.product_id for p in selected]
        row_numbers = [p.row_number for p in selected]
        sheets_manager.mark_products_used(row_numbers, today)
        logger.info(f"Marked {len(product_ids)} products as USED")
        
        logger.info("=" * 60)
        logger.info("SUCCESS! CSV generated and products updated")
        logger.info(f"Output file: {filepath}")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"ERROR: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

