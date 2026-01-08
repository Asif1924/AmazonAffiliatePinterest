# Quick Start Guide - Amazon Affiliate Link Fetcher

## What This Does

Automatically searches Amazon.ca for all 30 products in your Excel file and gets affiliate links.

## Quick Start

1. **Run the script:**
   ```bash
   python3 get_amazon_affiliate_links.py --tag your-affiliate-tag-20
   ```
   
   Replace `your-affiliate-tag-20` with your actual Amazon Associates tag.

2. **Log in to Amazon:**
   - Chrome browser will open to Amazon.ca
   - You have **60 seconds** to log in to your Amazon Associates account
   - Watch the countdown in the terminal
   
3. **Wait for completion:**
   - The script will automatically search for all 30 products
   - You'll see it working in the browser
   - Takes about 3-5 minutes total
   
4. **Get your results:**
   - Updated file: `products/Amazon Affiliate Pinterest Products_updated.xlsx`
   - Check the `AmazonAffiliateURL` column for all the affiliate links

## Your Products

The script will process these 30 products from your Excel file:

1. Anker PowerCore 20000mAh Power Bank
2. Instant Pot Duo 7-in-1 Electric Pressure Cooker
3. Resistance Bands Set with Handles
4. DEWALT 20V MAX Cordless Drill Combo Kit
5. VIOFO Dash Cam Front and Rear Camera
6. Logitech MX Master 3 Wireless Mouse
7. Apple AirPods Pro 2nd Generation
8. Ninja Air Fryer 4-Quart
9. Fitbit Charge 6 Fitness Tracker
10. BLACK+DECKER 20V MAX Cordless Drill
11. WeatherTech All-Weather Floor Mats
12. Mechanical Keyboard RGB Backlit
13. Samsung 65-Inch 4K Smart TV
14. Keurig K-Elite Coffee Maker
15. Yoga Mat Extra Thick Non-Slip
16. Craftsman 230-Piece Mechanics Tool Set
17. Garmin DriveSmart 65 GPS Navigator
18. USB-C Hub 7-in-1 Adapter
19. Bose QuietComfort 45 Headphones
20. Vitamix E310 Explorian Blender
21. Bowflex SelectTech Adjustable Dumbbells
22. Bosch 12V Cordless Drill Driver Kit
23. Armor All Car Vacuum Cleaner
24. Webcam 1080P HD with Microphone
25. Ring Video Doorbell Pro 2
26. Lodge Cast Iron Skillet 12-Inch
27. Foam Roller for Muscle Recovery
28. Milwaukee M18 Impact Driver Kit
29. Michelin Stealth Hybrid Wiper Blades
30. Standing Desk Converter

## What Happens

```
1. Script starts
   ↓
2. Opens Chrome → Amazon.ca
   ↓
3. 60-second pause (YOU LOG IN HERE)
   ↓
4. Searches for Product #1
   ↓
5. Gets affiliate link
   ↓
6. Waits 3 seconds
   ↓
7. Repeats for all 30 products
   ↓
8. Saves updated Excel file
   ↓
9. Done! ✅
```

## Important Notes

- **Don't close the browser** - let the script finish
- **Stay logged in** - don't log out during the process
- **Be patient** - it takes 3-5 minutes for all 30 products
- **Check the log** - `amazon_affiliate_links.log` has all details

## Troubleshooting

**"No module named 'selenium'"**
- Already installed! Just run the script.

**Browser doesn't open**
- Make sure Chrome is installed
- Try running again

**Can't find products**
- Product names might be too generic
- Check the log file for details
- The script will continue with other products

**Amazon shows CAPTCHA**
- You're logged in, so this is less likely
- If it happens, solve it manually
- Script will continue after you solve it

## Need Help?

Check the full documentation: `AMAZON_AFFILIATE_LINK_FETCHER_README.md`

