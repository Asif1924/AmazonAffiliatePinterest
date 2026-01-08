#!/usr/bin/env python3
"""
create_sample_products.py

Creates a sample Excel file with test products for testing the affiliate link fetcher.
"""

import pandas as pd
from pathlib import Path

# Sample products to test with
sample_products = [
    {
        'ProductID': 'ELEC001',
        'Niche': 'Electronics',
        'ProductName': 'Sony WH-1000XM4 Wireless Headphones',
        'Brand': 'Sony',
        'KeyBenefit': 'Industry-leading noise cancellation',
        'TopFeatures': 'Noise cancellation, 30hr battery, touch controls',
        'IdealFor': 'Travelers, music lovers, remote workers',
        'Keywords': 'wireless headphones, noise cancelling, Sony',
        'PriceBand': 'Premium',
        'AmazonAffiliateURL': '',
        'DisclosureLine': 'As an Amazon Associate I earn from qualifying purchases. #ad',
        'Angle': 'Problem-Solution',
        'HookStyle': 'Question',
        'TemplateID': 'T1',
        'BackgroundTheme': 'Tech Blue',
        'Status': 'READY',
        'LastUsedDate': '',
        'Priority': 5,
        'PinTitle': '',
        'PinHookOverlay': '',
        'PinDescription': '',
        'BoardName': 'Tech Gadgets',
        'CanvaImageName': ''
    },
    {
        'ProductID': 'HOME001',
        'Niche': 'Home & Kitchen',
        'ProductName': 'Instant Pot Duo 7-in-1 Electric Pressure Cooker',
        'Brand': 'Instant Pot',
        'KeyBenefit': 'Cooks meals 70% faster',
        'TopFeatures': '7-in-1 functionality, 6 quart capacity, easy to clean',
        'IdealFor': 'Busy families, meal preppers, home cooks',
        'Keywords': 'instant pot, pressure cooker, kitchen appliance',
        'PriceBand': 'Mid',
        'AmazonAffiliateURL': '',
        'DisclosureLine': 'As an Amazon Associate I earn from qualifying purchases. #ad',
        'Angle': 'Time-Saver',
        'HookStyle': 'Benefit',
        'TemplateID': 'T2',
        'BackgroundTheme': 'Kitchen Warm',
        'Status': 'READY',
        'LastUsedDate': '',
        'Priority': 4,
        'PinTitle': '',
        'PinHookOverlay': '',
        'PinDescription': '',
        'BoardName': 'Kitchen Essentials',
        'CanvaImageName': ''
    },
    {
        'ProductID': 'FIT001',
        'Niche': 'Fitness',
        'ProductName': 'Fitbit Charge 5 Fitness Tracker',
        'Brand': 'Fitbit',
        'KeyBenefit': 'Track your health 24/7',
        'TopFeatures': 'Heart rate monitor, GPS, sleep tracking, 7-day battery',
        'IdealFor': 'Fitness enthusiasts, health-conscious individuals',
        'Keywords': 'fitness tracker, fitbit, health monitor',
        'PriceBand': 'Mid',
        'AmazonAffiliateURL': '',
        'DisclosureLine': 'As an Amazon Associate I earn from qualifying purchases. #ad',
        'Angle': 'Health & Wellness',
        'HookStyle': 'Transformation',
        'TemplateID': 'T3',
        'BackgroundTheme': 'Fitness Green',
        'Status': 'READY',
        'LastUsedDate': '',
        'Priority': 5,
        'PinTitle': '',
        'PinHookOverlay': '',
        'PinDescription': '',
        'BoardName': 'Fitness & Health',
        'CanvaImageName': ''
    }
]

def create_sample_file():
    """Create a sample Excel file with test products"""
    
    # Create DataFrame
    df = pd.DataFrame(sample_products)
    
    # Save to Excel
    output_path = Path('products/Amazon Affiliate Pinterest Products_SAMPLE.xlsx')
    output_path.parent.mkdir(exist_ok=True)
    
    df.to_excel(output_path, index=False)
    
    print(f"✅ Sample file created: {output_path}")
    print(f"📊 Contains {len(sample_products)} sample products:")
    for i, product in enumerate(sample_products, 1):
        print(f"   {i}. {product['ProductName']}")
    print("\nYou can now test the affiliate link fetcher with:")
    print(f"   python3 get_amazon_affiliate_links.py --excel {output_path}")

if __name__ == "__main__":
    create_sample_file()

