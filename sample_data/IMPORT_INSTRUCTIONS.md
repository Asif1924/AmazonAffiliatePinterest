# How to Import Sample Data into Google Sheets

## Quick Import Method

### Step 1: Create a New Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Click "Blank" to create a new spreadsheet
3. Name it: "Amazon Affiliate Pinterest Products"

### Step 2: Import Products Data

1. In your new Google Sheet, click **File** → **Import**
2. Click **Upload** tab
3. Drag and drop `products_sample.csv` or click **Browse** to select it
4. In the import dialog:
   - **Import location**: Select "Replace current sheet"
   - **Separator type**: Select "Comma"
   - **Convert text to numbers, dates, and formulas**: Check this box
5. Click **Import data**

### Step 3: Rename the Sheet

1. Right-click on the sheet tab at the bottom (probably says "Sheet1")
2. Click **Rename**
3. Type: **Products**
4. Press Enter

### Step 4: Add the Formulas

The CSV doesn't include the auto-generated columns (S, T, U, V, W). Add these formulas:

**Cell S2** - Pin Title:
```
=IF(C2="","",C2 & " — " & IF(L2="Upgrade","Easy upgrade for ","Best pick for ") & G2)
```

**Cell T2** - Pin Hook Overlay:
```
=IF(C2="","",IF(M2="Question","Still dealing with " & LOWER(REGEXREPLACE(SPLIT(H2,",",TRUE,TRUE),"\s+$","")) & "?",IF(M2="Bold Claim","Fix this in 5 minutes",IF(M2="Stop Doing This","Stop struggling with this",IF(M2="3 Things","3 reasons you'll love this","Best pick for " & G2)))))
```

**Cell U2** - Pin Description:
```
=IF(C2="","","Why it's worth it: " & E2 & " Features: " & SUBSTITUTE(F2,";"," • ") & ". Great for: " & G2 & ". Keywords: " & H2 & " " & K2)
```

**Cell V2** - Board Name:
```
=IF(B2="","",IFERROR(VLOOKUP(B2,Boards!A:B,2,FALSE),"General Finds"))
```

**Cell W2** - Image Filename:
```
=IF(A2="","",TEXT(TODAY(),"yyyy-mm-dd") & "_" & N2 & "_" & A2 & ".png")
```

**Then**: Select cells S2:W2, and drag the fill handle down to row 31 to copy formulas to all products.

### Step 5: Create Boards Worksheet

1. Click the **+** button at the bottom left to add a new sheet
2. Rename it to: **Boards**
3. Click **File** → **Import**
4. Upload `boards_sample.csv`
5. Import location: Select "Replace current sheet"
6. Click **Import data**

### Step 6: Add Column Headers for Auto-Generated Fields

Go back to the **Products** sheet and add these headers in row 1:

- **S1**: PinTitle
- **T1**: PinHookOverlay
- **U1**: PinDescription
- **V1**: BoardName
- **W1**: CanvaImageName

### Step 7: Get Your Sheet ID

1. Look at the URL of your Google Sheet
2. It looks like: `https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit`
3. Copy the `SHEET_ID_HERE` part
4. Save it - you'll need it for `config.py`

## What's Included

### Products Sample (30 products)

The sample includes:
- **5 products** from each niche (electronics, home/kitchen, tools, fitness, cars, computer accessories)
- Mix of **price bands**: budget, mid, premium
- Various **angles**: Problem/Solution, Upgrade, Gift, Comparison, Quick Tip
- Different **hook styles**: Question, Bold Claim, Stop Doing This, 3 Things, Best For
- All **templates** represented: T1-T5
- **Priority** levels from 3-5
- All products set to **READY** status

### Boards Sample (6 boards)

Maps each niche to a Pinterest board name.

## Important Notes

### ⚠️ Replace Affiliate URLs

All products have placeholder URLs: `https://www.amazon.com/dp/XXXXXXX?tag=yourtag-20`

**You MUST replace these with your actual Amazon affiliate links:**

1. Go to [Amazon Associates](https://affiliate-program.amazon.com/)
2. Search for each product
3. Generate your affiliate link
4. Replace the placeholder URL in column J

### ⚠️ Customize Products

These are sample products. You should:
- Replace with products you actually want to promote
- Use real product names and features
- Add your own product research
- Verify all information is accurate

### ✅ What's Ready to Use

- Column structure is correct
- Formulas will work once added
- Data format is correct
- All required fields are filled
- Niches match board mappings

## Testing the Setup

After importing:

1. Check that formulas in columns S-W are working
2. Verify BoardName (column V) shows correct board for each niche
3. Check that CanvaImageName (column W) shows today's date
4. Make sure all 30 products are visible
5. Verify the Boards sheet has 6 rows (plus header)

## Next Steps

1. ✅ Import the sample data
2. ✅ Add the formulas
3. ✅ Get your Sheet ID
4. ✅ Share the sheet with your Google Service Account email
5. ✅ Update `config.py` with your Sheet ID
6. ✅ Replace placeholder affiliate URLs with real ones
7. ✅ Test the script: `python3 daily_canva_csv.py`

## Alternative: Manual Entry

If you prefer to enter data manually instead of importing:

1. Create the Products sheet with headers A-W
2. Copy the column headers from `docs/GOOGLE_SHEETS_SETUP.md`
3. Add the formulas to columns S-W
4. Enter products one by one using the examples as a guide
5. Create the Boards sheet and enter the 6 niche mappings

## Troubleshooting

**Formulas not working?**
- Make sure the Boards sheet exists and is named exactly "Boards"
- Check that column letters match (A=ProductID, B=Niche, etc.)
- Verify you're on row 2 when adding formulas (row 1 is headers)

**Import failed?**
- Make sure you selected "Comma" as separator
- Try opening the CSV in a text editor to verify format
- Check that the file downloaded completely

**BoardName showing #REF! error?**
- The Boards sheet doesn't exist or is named incorrectly
- Create the Boards sheet first, then add the formula

---

**You now have 30 sample products ready to test the system!** 🎉

