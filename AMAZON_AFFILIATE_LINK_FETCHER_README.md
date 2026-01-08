# Amazon Affiliate Link Fetcher

This Python script automatically searches for products on Amazon.ca and retrieves affiliate links for products listed in your Excel file.

## Features

- ✅ Reads product names from Excel file (Column C - ProductName)
- ✅ Automatically searches Amazon.ca for each product
- ✅ Retrieves the first matching product URL
- ✅ Generates Amazon affiliate links with your tag
- ✅ Updates the Excel file with affiliate URLs
- ✅ Detailed logging of all operations
- ✅ Handles errors gracefully

## Prerequisites

The required packages have already been installed:
- `openpyxl` - For reading/writing Excel files
- `pandas` - For data manipulation
- `selenium` - For web automation
- `webdriver-manager` - For automatic ChromeDriver management

## Usage

### Basic Usage (without affiliate tag)

```bash
python3 get_amazon_affiliate_links.py
```

This will:
1. Read `products/Amazon Affiliate Pinterest Products.xlsx`
2. Search for each product on Amazon.ca
3. Save results to `products/Amazon Affiliate Pinterest Products_updated.xlsx`

### With Affiliate Tag

```bash
python3 get_amazon_affiliate_links.py --tag your-affiliate-tag-20
```

Replace `your-affiliate-tag-20` with your actual Amazon Associates tag.

### Custom Excel File

```bash
python3 get_amazon_affiliate_links.py --excel path/to/your/file.xlsx --tag your-tag-20
```

### Custom Output File

```bash
python3 get_amazon_affiliate_links.py --output path/to/output.xlsx --tag your-tag-20
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--excel` | Path to input Excel file | `products/Amazon Affiliate Pinterest Products.xlsx` |
| `--tag` | Your Amazon affiliate tag | None (generates clean URLs) |
| `--output` | Path to output Excel file | Adds `_updated` to input filename |

## How It Works

1. **Load Excel**: Reads the "Products" sheet from the Excel file and finds all rows with ProductName values
2. **Setup Browser**: Launches Chrome browser (you'll see it open)
3. **Login Pause**: Opens Amazon.ca and pauses for 60 seconds so you can log in to your Amazon Associates account
4. **Search Products**: For each product:
   - Goes to Amazon.ca
   - Searches for the product name
   - Finds the first matching result
   - Extracts the product URL
   - Generates affiliate link with your tag (if provided)
5. **Update Excel**: Saves all affiliate URLs to the AmazonAffiliateURL column
6. **Save Results**: Creates a new Excel file with updated data (preserves all sheets)

## Excel File Format

The script expects:
- A sheet named **"Products"** in your Excel file
- **Column C (ProductName)**: The name of the product to search for
- **Column J (AmazonAffiliateURL)**: Where the affiliate link will be saved

All other sheets in the Excel file will be preserved in the output file.

## Logging

All operations are logged to:
- Console (terminal output)
- `amazon_affiliate_links.log` file

Check the log file for detailed information about each product search.

## Example Output

```
Processing product 1/5: Wireless Bluetooth Headphones
Found product URL: https://www.amazon.ca/dp/B08XYZ1234
Generated affiliate link: https://www.amazon.ca/dp/B08XYZ1234?tag=yourtag-20

Processing product 2/5: USB-C Charging Cable
Found product URL: https://www.amazon.ca/dp/B09ABC5678
Generated affiliate link: https://www.amazon.ca/dp/B09ABC5678?tag=yourtag-20
```

## Important Notes

### Login Process
- When the script starts, it will open Amazon.ca in Chrome
- You have **60 seconds** to log in to your Amazon Associates account
- The script will show a countdown timer in the terminal
- After 60 seconds, it will automatically start searching for products
- Stay logged in throughout the entire process

### Browser Window
- The script will open a Chrome browser window
- You'll see it navigate to Amazon and search for products
- Don't close the browser manually - let the script finish
- To run without seeing the browser, uncomment the headless option in the code

### Rate Limiting
- The script adds a 3-second delay between searches
- This is to be respectful to Amazon's servers
- Don't reduce this delay to avoid being blocked

### Amazon Captcha
- If Amazon shows a CAPTCHA, the script may fail
- This can happen if you run it too frequently
- Solution: Wait a few minutes and try again

### Product Matching
- The script selects the FIRST search result
- Make sure your product names are specific enough
- Example: "Sony WH-1000XM4" is better than "headphones"

## Troubleshooting

### "No products to process"
- Your Excel file has no ProductName values in Column C
- Add product names and try again

### "Chrome driver not found"
- The script should auto-download ChromeDriver
- Make sure you have Chrome browser installed

### "Product not found"
- The product name might be too generic
- Try making it more specific (include brand, model)

### Script hangs or freezes
- Amazon might be showing a CAPTCHA
- Close the browser and wait a few minutes
- Try again with fewer products

## Getting Your Amazon Affiliate Tag

1. Sign up for Amazon Associates: https://affiliate-program.amazon.ca/
2. After approval, your tag will look like: `yourname-20`
3. Use this tag with the `--tag` option

## Example Workflow

1. Add product names to your Excel file in Column C
2. Run the script:
   ```bash
   python3 get_amazon_affiliate_links.py --tag myamazon-20
   ```
3. Wait for the script to complete (you'll see the browser working)
4. Check the output file: `products/Amazon Affiliate Pinterest Products_updated.xlsx`
5. The AmazonAffiliateURL column will be populated with affiliate links

## Support

For issues or questions:
- Check the log file: `amazon_affiliate_links.log`
- Make sure Chrome browser is installed
- Verify your Excel file has the correct format

