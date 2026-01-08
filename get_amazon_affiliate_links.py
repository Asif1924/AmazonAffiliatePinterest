#!/usr/bin/env python3
"""
get_amazon_affiliate_links.py

Reads products from Excel file, searches Amazon.ca for each product,
and retrieves SiteStripe affiliate links.

Requirements:
- openpyxl
- pandas
- selenium
- webdriver-manager
"""

import pandas as pd
import time
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('amazon_affiliate_links.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AmazonAffiliateLinkFetcher:
    """Fetches Amazon affiliate links for products"""
    
    def __init__(self, excel_path: str, affiliate_tag: str = None):
        """
        Initialize the fetcher
        
        Args:
            excel_path: Path to the Excel file
            affiliate_tag: Your Amazon affiliate tag (e.g., 'yourtag-20')
        """
        self.excel_path = Path(excel_path)
        self.affiliate_tag = affiliate_tag
        self.driver = None
        self.df = None
        
    def setup_driver(self):
        """Setup Chrome WebDriver with options"""
        logger.info("Setting up Chrome WebDriver...")

        chrome_options = Options()
        # Uncomment the next line to run headless (no browser window)
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Set user agent to avoid detection
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

        logger.info("WebDriver setup complete")

        # Navigate to Amazon.ca and pause for login
        logger.info("Opening Amazon.ca...")
        self.driver.get("https://www.amazon.ca")

        print("\n" + "="*70)
        print("🔐 AMAZON LOGIN REQUIRED")
        print("="*70)
        print("The browser has opened Amazon.ca")
        print("Please log in to your Amazon Associates account now.")
        print("\nYou have 60 seconds to complete the login.")
        print("="*70 + "\n")

        # Countdown timer
        for remaining in range(60, 0, -10):
            logger.info(f"Waiting for login... {remaining} seconds remaining")
            print(f"⏳ {remaining} seconds remaining...")
            time.sleep(10)

        print("\n✅ Proceeding with product searches...\n")
        logger.info("Login wait period complete, starting product searches")
        
    def load_excel(self):
        """Load the Excel file"""
        logger.info(f"Loading Excel file: {self.excel_path}")

        if not self.excel_path.exists():
            raise FileNotFoundError(f"Excel file not found: {self.excel_path}")

        # Read from the "Products" sheet
        self.df = pd.read_excel(self.excel_path, sheet_name='Products')
        logger.info(f"Loaded {len(self.df)} rows from Excel (Products sheet)")

        # Filter rows with ProductName
        self.df = self.df[self.df['ProductName'].notna()]
        logger.info(f"Found {len(self.df)} products with names")
        
    def search_amazon_product(self, product_name: str) -> str:
        """
        Search for a product on Amazon.ca and get the first result URL
        
        Args:
            product_name: Name of the product to search
            
        Returns:
            Product URL or None if not found
        """
        try:
            logger.info(f"Searching for: {product_name}")
            
            # Go to Amazon.ca
            self.driver.get("https://www.amazon.ca")
            time.sleep(2)
            
            # Find search box and enter product name
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.clear()
            search_box.send_keys(product_name)
            search_box.send_keys(Keys.RETURN)
            
            # Wait for results to load
            time.sleep(3)
            
            # Find the first product result
            # Amazon uses different selectors, trying multiple approaches
            selectors = [
                "h2 a.a-link-normal.s-no-outline",
                "h2 a.a-link-normal",
                "[data-component-type='s-search-result'] h2 a",
                ".s-result-item h2 a"
            ]
            
            product_link = None
            for selector in selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        product_link = elements[0].get_attribute('href')
                        break
                except:
                    continue
            
            if product_link:
                logger.info(f"Found product URL: {product_link}")
                return product_link
            else:
                logger.warning(f"No product found for: {product_name}")
                return None
                
        except Exception as e:
            logger.error(f"Error searching for {product_name}: {e}")
            return None
    
    def get_affiliate_link(self, product_url: str) -> str:
        """
        Convert a regular Amazon URL to an affiliate link
        
        Args:
            product_url: Regular Amazon product URL
            
        Returns:
            Affiliate link with tag
        """
        if not product_url:
            return None
        
        # Extract ASIN from URL
        # Amazon URLs typically contain /dp/ASIN or /gp/product/ASIN
        import re
        asin_match = re.search(r'/dp/([A-Z0-9]{10})', product_url)
        if not asin_match:
            asin_match = re.search(r'/gp/product/([A-Z0-9]{10})', product_url)
        
        if asin_match:
            asin = asin_match.group(1)
            if self.affiliate_tag:
                affiliate_link = f"https://www.amazon.ca/dp/{asin}?tag={self.affiliate_tag}"
            else:
                affiliate_link = f"https://www.amazon.ca/dp/{asin}"
            
            logger.info(f"Generated affiliate link: {affiliate_link}")
            return affiliate_link
        else:
            logger.warning(f"Could not extract ASIN from URL: {product_url}")
            return product_url

    def process_products(self):
        """Process all products and get affiliate links"""
        if self.df is None or len(self.df) == 0:
            logger.warning("No products to process")
            return

        logger.info(f"Processing {len(self.df)} products...")

        results = []
        for idx, row in self.df.iterrows():
            product_name = row['ProductName']
            logger.info(f"\n{'='*60}")
            logger.info(f"Processing product {idx + 1}/{len(self.df)}: {product_name}")
            logger.info(f"{'='*60}")

            # Search for product
            product_url = self.search_amazon_product(product_name)

            # Get affiliate link
            affiliate_link = self.get_affiliate_link(product_url)

            # Store result
            results.append({
                'ProductName': product_name,
                'ProductURL': product_url,
                'AffiliateURL': affiliate_link
            })

            # Update the dataframe
            self.df.at[idx, 'AmazonAffiliateURL'] = affiliate_link

            # Be nice to Amazon - add delay between requests
            time.sleep(3)

        return results

    def save_results(self, output_path: str = None):
        """Save updated Excel file, preserving all sheets"""
        if output_path is None:
            output_path = self.excel_path.parent / f"{self.excel_path.stem}_updated{self.excel_path.suffix}"

        logger.info(f"Saving results to: {output_path}")

        # Read all sheets from the original file
        with pd.ExcelFile(self.excel_path) as xls:
            # Create a writer object
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                # Copy all sheets except Products
                for sheet_name in xls.sheet_names:
                    if sheet_name == 'Products':
                        # Write our updated Products sheet
                        self.df.to_excel(writer, sheet_name='Products', index=False)
                    else:
                        # Copy other sheets as-is
                        df_sheet = pd.read_excel(xls, sheet_name=sheet_name)
                        df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)

        logger.info("Results saved successfully")

        return output_path

    def cleanup(self):
        """Close the browser"""
        if self.driver:
            logger.info("Closing browser...")
            self.driver.quit()

    def run(self):
        """Main execution flow"""
        try:
            self.load_excel()
            self.setup_driver()
            results = self.process_products()
            output_path = self.save_results()

            logger.info("\n" + "="*60)
            logger.info("PROCESSING COMPLETE")
            logger.info("="*60)
            logger.info(f"Updated file saved to: {output_path}")
            logger.info(f"Total products processed: {len(results)}")

            return results

        except Exception as e:
            logger.error(f"Error during execution: {e}", exc_info=True)
            raise
        finally:
            self.cleanup()


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Fetch Amazon affiliate links for products in Excel file'
    )
    parser.add_argument(
        '--excel',
        default='products/Amazon Affiliate Pinterest Products.xlsx',
        help='Path to Excel file (default: products/Amazon Affiliate Pinterest Products.xlsx)'
    )
    parser.add_argument(
        '--tag',
        help='Your Amazon affiliate tag (e.g., yourtag-20)'
    )
    parser.add_argument(
        '--output',
        help='Output file path (default: adds _updated to input filename)'
    )

    args = parser.parse_args()

    # Create fetcher instance
    fetcher = AmazonAffiliateLinkFetcher(
        excel_path=args.excel,
        affiliate_tag=args.tag
    )

    # Run the process
    results = fetcher.run()

    print("\n" + "="*60)
    print("SUCCESS!")
    print("="*60)
    print(f"Processed {len(results)} products")
    print("\nResults:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['ProductName']}")
        print(f"   URL: {result['AffiliateURL']}")


if __name__ == "__main__":
    main()

