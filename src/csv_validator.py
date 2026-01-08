"""
CSV validation logic
"""

import csv
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class CSVValidator:
    """Validates generated CSV content"""
    
    def __init__(self, required_columns: List[str], required_disclosure: str):
        """
        Initialize CSV validator
        
        Args:
            required_columns: List of required column names
            required_disclosure: Required disclosure text in DESC
        """
        self.required_columns = required_columns
        self.required_disclosure = required_disclosure
    
    def validate(self, csv_text: str, expected_rows: int) -> List[Dict[str, str]]:
        """
        Validate CSV text and return parsed rows
        
        Args:
            csv_text: CSV text to validate
            expected_rows: Expected number of data rows
        
        Returns:
            List of validated row dictionaries
        
        Raises:
            ValueError: If validation fails
        """
        # Parse CSV
        rows = self._parse_csv(csv_text)
        
        # Validate row count
        if len(rows) != expected_rows:
            raise ValueError(
                f"Expected {expected_rows} rows, got {len(rows)}. "
                "LLM may have generated incorrect output."
            )
        
        # Validate each row
        for i, row in enumerate(rows, 1):
            self._validate_row(row, i)
        
        logger.info(f"CSV validation passed: {len(rows)} rows validated")
        return rows
    
    def _parse_csv(self, csv_text: str) -> List[Dict[str, str]]:
        """
        Parse CSV text into list of dictionaries
        
        Args:
            csv_text: CSV text
        
        Returns:
            List of row dictionaries
        
        Raises:
            ValueError: If CSV parsing fails
        """
        try:
            lines = csv_text.strip().split('\n')
            reader = csv.DictReader(lines)
            
            # Check header
            header = reader.fieldnames
            if not header:
                raise ValueError("CSV has no header row")

            logger.debug(f"CSV header found: {header}")
            logger.debug(f"Required columns: {self.required_columns}")

            # Validate required columns
            missing = set(self.required_columns) - set(header)
            if missing:
                raise ValueError(
                    f"Missing required columns: {', '.join(sorted(missing))}. "
                    f"Found columns: {', '.join(header)}"
                )
            
            # Parse rows
            rows = list(reader)
            return rows
            
        except csv.Error as e:
            raise ValueError(f"CSV parsing error: {e}")
        except Exception as e:
            raise ValueError(f"Failed to parse CSV: {e}")
    
    def _validate_row(self, row: Dict[str, str], row_num: int):
        """
        Validate a single row
        
        Args:
            row: Row dictionary
            row_num: Row number (for error messages)
        
        Raises:
            ValueError: If validation fails
        """
        # Check HOOK
        hook = row.get('HOOK', '').strip()
        if not hook:
            raise ValueError(f"Row {row_num}: HOOK is empty")
        
        hook_words = len(hook.split())
        if hook_words < 3 or hook_words > 7:
            logger.warning(
                f"Row {row_num}: HOOK has {hook_words} words "
                "(recommended: 3-7)"
            )
        
        # Check TITLE
        title = row.get('TITLE', '').strip()
        if not title:
            raise ValueError(f"Row {row_num}: TITLE is empty")
        
        title_len = len(title)
        if title_len < 40 or title_len > 70:
            logger.warning(
                f"Row {row_num}: TITLE has {title_len} chars "
                "(recommended: 40-70)"
            )
        
        # Check DESC
        desc = row.get('DESC', '').strip()
        if not desc:
            raise ValueError(f"Row {row_num}: DESC is empty")
        
        if self.required_disclosure not in desc:
            raise ValueError(
                f"Row {row_num}: DESC missing required disclosure: "
                f"{self.required_disclosure}"
            )
        
        # Check URL
        url = row.get('URL', '').strip()
        if not url:
            raise ValueError(f"Row {row_num}: URL is empty")
        
        if not url.startswith('http'):
            raise ValueError(f"Row {row_num}: URL is invalid (must start with http)")
        
        # Check FILENAME
        filename = row.get('FILENAME', '').strip()
        if not filename:
            raise ValueError(f"Row {row_num}: FILENAME is empty")
        
        # Check BOARD
        board = row.get('BOARD', '').strip()
        if not board:
            raise ValueError(f"Row {row_num}: BOARD is empty")

