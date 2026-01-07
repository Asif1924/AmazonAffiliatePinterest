# Sample Data for Amazon Affiliate Pinterest Automation

This folder contains ready-to-import sample data for your Google Sheets.

## 📁 Files Included

### 1. `products_sample.csv`
**30 sample products** across all 6 niches:
- 5 Electronics products
- 5 Home/Kitchen products  
- 5 Tools products
- 5 Fitness products
- 5 Car accessories products
- 5 Computer accessories products

**Features:**
- All required columns (A-R) filled in
- Mix of price bands (budget, mid, premium)
- Various angles and hook styles
- All templates (T1-T5) represented
- Priority levels 3-5
- All set to READY status

### 2. `boards_sample.csv`
**6 Pinterest board mappings** for each niche

### 3. `IMPORT_INSTRUCTIONS.md`
**Step-by-step guide** for importing into Google Sheets

## 🚀 Quick Start

### Option 1: Import CSV Files (Recommended - 5 minutes)

1. Create a new Google Sheet
2. Import `products_sample.csv` → rename sheet to "Products"
3. Add formulas to columns S, T, U, V, W (see IMPORT_INSTRUCTIONS.md)
4. Create new sheet, import `boards_sample.csv` → rename to "Boards"
5. Get your Sheet ID from the URL
6. Done! ✅

### Option 2: Copy-Paste (10 minutes)

1. Open `products_sample.csv` in Excel or Google Sheets
2. Copy all data
3. Paste into your Google Sheet "Products" tab
4. Add formulas to columns S-W
5. Repeat for `boards_sample.csv` → "Boards" tab

## ⚠️ Important: Replace Placeholder Data

### Before Using in Production:

1. **Replace ALL affiliate URLs** in column J
   - Current: `https://www.amazon.com/dp/XXXXXXX?tag=yourtag-20`
   - Replace with your actual Amazon Associate links

2. **Customize products** (optional but recommended)
   - Use products you actually want to promote
   - Verify product details are accurate
   - Add your own product research

3. **Share with Service Account**
   - Share your Google Sheet with the service account email
   - Give "Editor" permissions

## 📊 Sample Data Overview

### Products by Niche
| Niche | Count | Example Products |
|-------|-------|------------------|
| Electronics | 5 | Anker Power Bank, Apple AirPods, Samsung TV, Bose Headphones, Ring Doorbell |
| Home/Kitchen | 5 | Instant Pot, Ninja Air Fryer, Keurig Coffee Maker, Vitamix Blender, Lodge Skillet |
| Tools | 5 | DEWALT Drill, BLACK+DECKER Drill, Craftsman Tool Set, Bosch Drill, Milwaukee Impact |
| Fitness | 5 | Resistance Bands, Fitbit Tracker, Yoga Mat, Bowflex Dumbbells, Foam Roller |
| Cars | 5 | VIOFO Dash Cam, WeatherTech Mats, Garmin GPS, Armor All Vacuum, Michelin Wipers |
| Computer Accessories | 5 | Logitech Mouse, Mechanical Keyboard, USB-C Hub, Webcam, Standing Desk |

### Products by Price Band
- **Budget** (8 products): $20-50 range
- **Mid** (14 products): $50-150 range  
- **Premium** (8 products): $150+ range

### Products by Priority
- **Priority 5** (8 products): Top performers
- **Priority 4** (12 products): Good performers
- **Priority 3** (10 products): Testing/rotation

## ✅ What's Correct

- ✅ All 18 columns (A-R) properly filled
- ✅ Proper data format and structure
- ✅ Disclosure text in column K
- ✅ Valid niche values matching Boards sheet
- ✅ Proper angle and hook style values
- ✅ Template IDs (T1-T5) assigned
- ✅ All products set to READY status
- ✅ Priority values assigned (3-5)

## 🔧 After Import: Add Formulas

Don't forget to add these formulas to the Products sheet:

**Column S (PinTitle)** - Row 2:
```
=IF(C2="","",C2 & " — " & IF(L2="Upgrade","Easy upgrade for ","Best pick for ") & G2)
```

**Column T (PinHookOverlay)** - Row 2:
```
=IF(C2="","",IF(M2="Question","Still dealing with " & LOWER(REGEXREPLACE(SPLIT(H2,",",TRUE,TRUE),"\s+$","")) & "?",IF(M2="Bold Claim","Fix this in 5 minutes",IF(M2="Stop Doing This","Stop struggling with this",IF(M2="3 Things","3 reasons you'll love this","Best pick for " & G2)))))
```

**Column U (PinDescription)** - Row 2:
```
=IF(C2="","","Why it's worth it: " & E2 & " Features: " & SUBSTITUTE(F2,";"," • ") & ". Great for: " & G2 & ". Keywords: " & H2 & " " & K2)
```

**Column V (BoardName)** - Row 2:
```
=IF(B2="","",IFERROR(VLOOKUP(B2,Boards!A:B,2,FALSE),"General Finds"))
```

**Column W (CanvaImageName)** - Row 2:
```
=IF(A2="","",TEXT(TODAY(),"yyyy-mm-dd") & "_" & N2 & "_" & A2 & ".png")
```

Then drag formulas down to row 31.

## 🧪 Testing

After importing and adding formulas:

1. **Test the script:**
   ```bash
   python3 daily_canva_csv.py
   ```

2. **Expected result:**
   - Script selects 10 products
   - Generates CSV in `daily_csv/`
   - Updates 10 products to USED status
   - Updates LastUsedDate to today

3. **Verify:**
   - Check `daily_csv/canva_bulk_YYYY-MM-DD.csv` exists
   - Open CSV - should have 10 rows
   - Check Google Sheet - 10 products now show USED

## 📚 Additional Resources

- **Full Setup Guide**: `../docs/GOOGLE_SHEETS_SETUP.md`
- **Import Instructions**: `IMPORT_INSTRUCTIONS.md`
- **Example Products**: `../docs/EXAMPLE_PRODUCTS.md`
- **Main README**: `../README.md`

## 💡 Tips

1. **Start with sample data** to test the system
2. **Replace URLs** before going live
3. **Add more products** gradually (aim for 50+)
4. **Track performance** and adjust priorities
5. **Refresh products** monthly with new items

---

**Ready to import? See `IMPORT_INSTRUCTIONS.md` for step-by-step guide!** 📊

