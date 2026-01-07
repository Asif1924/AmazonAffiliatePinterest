"""
Google Sheets integration
"""

import datetime as dt
import logging
from pathlib import Path
from typing import List, Dict, Any

import gspread
from google.oauth2.service_account import Credentials

logger = logging.getLogger(__name__)


class GoogleSheetsManager:
    """Manages Google Sheets operations"""
    
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    
    def __init__(self, sheet_id: str, credentials_file: str):
        """
        Initialize Google Sheets manager
        
        Args:
            sheet_id: Google Sheet ID
            credentials_file: Path to service account credentials JSON
        """
        self.sheet_id = sheet_id
        self.credentials_file = credentials_file
        self.client = None
        self.spreadsheet = None
        self._connect()
    
    def _connect(self):
        """Connect to Google Sheets"""
        try:
            creds_path = Path(self.credentials_file)
            if not creds_path.exists():
                raise FileNotFoundError(
                    f"Credentials file not found: {self.credentials_file}\n"
                    "Please follow the setup instructions in README.md"
                )
            
            creds = Credentials.from_service_account_file(
                self.credentials_file,
                scopes=self.SCOPES
            )
            self.client = gspread.authorize(creds)
            self.spreadsheet = self.client.open_by_key(self.sheet_id)
            logger.info("Connected to Google Sheets successfully")
            
        except Exception as e:
            logger.error(f"Failed to connect to Google Sheets: {e}")
            raise
    
    def load_products(self) -> List[Any]:
        """
        Load products from the Products worksheet
        
        Returns:
            List of Product objects
        """
        from daily_canva_csv import Product
        
        try:
            worksheet = self.spreadsheet.worksheet("Products")
            records = worksheet.get_all_records()
            
            products = []
            for idx, row in enumerate(records, start=2):  # Start at 2 (row 1 is header)
                # Skip empty rows
                if not row.get('ProductID'):
                    continue
                
                product = Product(
                    product_id=str(row.get('ProductID', '')),
                    niche=str(row.get('Niche', '')),
                    name=str(row.get('ProductName', '')),
                    brand=str(row.get('Brand', '')),
                    key_benefit=str(row.get('KeyBenefit', '')),
                    features=str(row.get('TopFeatures', '')),
                    ideal_for=str(row.get('IdealFor', '')),
                    keywords=str(row.get('Keywords', '')),
                    price_band=str(row.get('PriceBand', '')),
                    affiliate_url=str(row.get('AmazonAffiliateURL', '')),
                    disclosure=str(row.get('DisclosureLine', '')),
                    angle=str(row.get('Angle', '')),
                    hook_style=str(row.get('HookStyle', '')),
                    template_id=str(row.get('TemplateID', '')),
                    background_theme=str(row.get('BackgroundTheme', '')),
                    status=str(row.get('Status', '')),
                    last_used_date=str(row.get('LastUsedDate', '')),
                    priority=int(row.get('Priority', 1)),
                    board=str(row.get('BoardName', '')),
                    filename=str(row.get('CanvaImageName', '')),
                    row_number=idx
                )
                products.append(product)
            
            logger.info(f"Loaded {len(products)} products from Google Sheets")
            return products
            
        except Exception as e:
            logger.error(f"Failed to load products: {e}")
            raise
    
    def mark_products_used(self, row_numbers: List[int], date: str):
        """
        Mark products as USED and update LastUsedDate
        
        Args:
            row_numbers: List of row numbers to update
            date: Date string (YYYY-MM-DD)
        """
        try:
            worksheet = self.spreadsheet.worksheet("Products")
            
            # Batch update for efficiency
            updates = []
            for row_num in row_numbers:
                # Column P = Status (column 16)
                # Column Q = LastUsedDate (column 17)
                updates.append({
                    'range': f'P{row_num}',
                    'values': [['USED']]
                })
                updates.append({
                    'range': f'Q{row_num}',
                    'values': [[date]]
                })
            
            worksheet.batch_update(updates)
            logger.info(f"Updated {len(row_numbers)} products to USED status")
            
        except Exception as e:
            logger.error(f"Failed to update products: {e}")
            raise

