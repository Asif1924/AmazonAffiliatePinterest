# ⚠️ IMPORTANT: Complete Your Google Sheet Setup

## The Issue

Your script ran successfully and connected to Google Sheets, but the **auto-generated columns are missing formulas**.

The error `FILENAME is empty` means column W (`CanvaImageName`) doesn't have the formula to generate filenames.

## What You Need to Do RIGHT NOW

### Step 1: Open Your Google Sheet

Your Sheet ID: `1XzB1Kw19cmAqmBcVsnLsE5MZ7xePaUrq72pNgxTNLp4`

Direct link: https://docs.google.com/spreadsheets/d/1XzB1Kw19cmAqmBcVsnLsE5MZ7xePaUrq72pNgxTNLp4/edit

### Step 2: Add Column Headers (if missing)

Make sure row 1 has these headers in columns S, T, U, V, W:

- **S1**: `PinTitle`
- **T1**: `PinHookOverlay`
- **U1**: `PinDescription`
- **V1**: `BoardName`
- **W1**: `CanvaImageName`

### Step 3: Add Formulas to Row 2

Copy and paste these formulas EXACTLY:

#### Cell S2 (PinTitle):
```
=IF(C2="","",C2 & " — " & IF(L2="Upgrade","Easy upgrade for ","Best pick for ") & G2)
```

#### Cell T2 (PinHookOverlay):
```
=IF(C2="","",IF(M2="Question","Still dealing with " & LOWER(REGEXREPLACE(SPLIT(H2,",",TRUE,TRUE),"\s+$","")) & "?",IF(M2="Bold Claim","Fix this in 5 minutes",IF(M2="Stop Doing This","Stop struggling with this",IF(M2="3 Things","3 reasons you'll love this","Best pick for " & G2)))))
```

#### Cell U2 (PinDescription):
```
=IF(C2="","","Why it's worth it: " & E2 & " Features: " & SUBSTITUTE(F2,";"," • ") & ". Great for: " & G2 & ". Keywords: " & H2 & " " & K2)
```

#### Cell V2 (BoardName):
```
=IF(B2="","",IFERROR(VLOOKUP(B2,Boards!A:B,2,FALSE),"General Finds"))
```

#### Cell W2 (CanvaImageName):
```
=IF(A2="","",TEXT(TODAY(),"yyyy-mm-dd") & "_" & N2 & "_" & A2 & ".png")
```

### Step 4: Copy Formulas Down

1. Select cells **S2:W2** (all 5 formulas)
2. Grab the small blue square at the bottom-right corner
3. Drag it down to row 31 (to cover all 30 products)
4. Release

All formulas should now be copied to all product rows!

### Step 5: Verify the Boards Sheet Exists

1. Look at the bottom of your Google Sheet
2. You should see two tabs: **Products** and **Boards**
3. If **Boards** tab is missing:
   - Click the **+** button to add a new sheet
   - Rename it to **Boards** (exact spelling, capital B)
   - Import the `sample_data/boards_sample.csv` file

The Boards sheet should have:
```
Niche,BoardName
electronics,Smart Electronics Finds
home/kitchen,Kitchen Upgrades & Must-Haves
tools,Tools That Save Time
fitness,Home Gym Essentials
cars,Car Accessories & Upgrades
computer accessories,Desk Setup & Accessories
```

### Step 6: Check Your Work

After adding formulas, check that:

- ✅ Column V (BoardName) shows board names like "Smart Electronics Finds"
- ✅ Column W (CanvaImageName) shows filenames like "2026-01-07_T1_PROD001.png"
- ✅ All 30 rows have formulas (not just row 2)
- ✅ No #REF! or #ERROR! messages

## Then Run the Script Again

```bash
source venv/bin/activate
python3 daily_canva_csv.py
```

It should work now! ✅

## Quick Visual Check

Your Products sheet should look like this:

| A | B | C | ... | S | T | U | V | W |
|---|---|---|-----|---|---|---|---|---|
| ProductID | Niche | ProductName | ... | PinTitle | PinHookOverlay | PinDescription | BoardName | CanvaImageName |
| PROD001 | electronics | Anker PowerCore... | ... | Anker PowerCore... | Still dealing with... | Why it's worth it... | Smart Electronics Finds | 2026-01-07_T1_PROD001.png |

## Need More Help?

See the detailed guide: `sample_data/IMPORT_INSTRUCTIONS.md`

---

**The script is working! You just need to add the formulas to your Google Sheet.** 🎯

