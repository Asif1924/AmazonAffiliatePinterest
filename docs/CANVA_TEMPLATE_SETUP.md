# Canva Template Setup Guide

## Overview

You'll create 5 Pinterest pin templates (T1-T5) in Canva that use Bulk Create functionality to generate multiple pins from CSV data.

## Pinterest Pin Dimensions

- **Standard Pinterest Pin**: 1000 x 1500 pixels (2:3 ratio)
- **Recommended**: Use this size for all templates

## Step 1: Create Your First Template (T1)

1. Go to [Canva.com](https://www.canva.com)
2. Click "Create a design"
3. Select "Pinterest Pin" (or custom size: 1000 x 1500 px)
4. Design your template with these elements:

### Required Text Placeholders

Add text boxes with these exact placeholder names (Canva will replace them with CSV data):

1. **{{HOOK}}** - Main attention-grabbing text
   - Position: Top third of the pin
   - Font: Large, bold, eye-catching
   - Size: 60-80pt
   - Color: High contrast with background
   - Example style: Bold sans-serif

2. **{{TITLE}}** - Product name and context
   - Position: Middle section
   - Font: Medium weight, readable
   - Size: 36-48pt
   - Color: Complementary to hook
   - Example style: Semi-bold sans-serif

3. **{{SUBTITLE}}** - Optional supporting text
   - Position: Below title
   - Font: Regular weight
   - Size: 24-32pt
   - Color: Slightly muted
   - Example style: Regular sans-serif or serif

4. **{{DESC}}** - Small description text (optional)
   - Position: Bottom section
   - Font: Small, readable
   - Size: 16-20pt
   - Color: Subtle but readable
   - Note: This often gets cut off on Pinterest, so it's optional

5. **{{URL}}** - Can be invisible or very small
   - Position: Bottom corner
   - Font: Tiny
   - Size: 8-10pt
   - Note: This is mainly for tracking in Canva

### Design Tips

- **Background**: Use solid colors, gradients, or subtle patterns
- **Contrast**: Ensure text is easily readable
- **Branding**: Add a small logo or watermark (optional)
- **Visual hierarchy**: HOOK should be most prominent
- **White space**: Don't overcrowd the design
- **On-brand**: Match your Pinterest aesthetic

### Example Layout (T1 - Clean Tech Style)

```
┌─────────────────────────┐
│                         │
│     {{HOOK}}            │  ← Large, bold, top
│                         │
│  ─────────────────      │
│                         │
│   {{TITLE}}             │  ← Medium, center
│                         │
│   {{SUBTITLE}}          │  ← Smaller, below title
│                         │
│                         │
│  [Product Image Area]   │  ← Optional: leave space for product
│                         │
│                         │
│  {{DESC}}               │  ← Small text, bottom
│                         │
└─────────────────────────┘
```

## Step 2: Set Up Bulk Create

1. In your Canva template, click "Apps" in the left sidebar
2. Search for "Bulk Create"
3. Click on the Bulk Create app
4. Click "Connect data"
5. Choose "Upload CSV"
6. Map your placeholders:
   - HOOK → {{HOOK}}
   - TITLE → {{TITLE}}
   - SUBTITLE → {{SUBTITLE}}
   - DESC → {{DESC}}
   - URL → {{URL}}
   - FILENAME → (used for naming downloads)
   - BOARD → (metadata, not displayed)

## Step 3: Create Templates T2-T5

Create 4 more templates with different styles:

### T2 - Bold Claim Style
- Bright, energetic colors
- Large text emphasis
- Minimal background elements
- Best for: "Bold Claim" hook style

### T3 - Problem/Solution Style
- Split design (problem vs solution)
- Before/after visual concept
- Contrasting colors
- Best for: "Problem/Solution" angle

### T4 - List Style
- Numbered or bulleted layout
- Clean, organized appearance
- Best for: "3 Things" hook style

### T5 - Minimal/Premium Style
- Lots of white space
- Elegant fonts
- Subtle colors
- Best for: Premium products

## Step 4: Save Templates

1. Save each template with a clear name:
   - "Pinterest Pin Template T1 - Clean Tech"
   - "Pinterest Pin Template T2 - Bold Claim"
   - etc.

2. Make copies before using Bulk Create (to preserve originals)

## Step 5: Using Bulk Create with Your CSV

1. Open your template
2. Click "Apps" → "Bulk Create"
3. Upload your `canva_bulk_YYYY-MM-DD.csv` file
4. Verify the data mapping
5. Click "Generate" (creates 10 pins)
6. Review all pins
7. Download all as PNG files
8. The filenames will match your {{FILENAME}} column

## CSV Format Expected by Canva

Your CSV must have this exact header:

```
HOOK,TITLE,SUBTITLE,DESC,URL,FILENAME,BOARD
```

Example row:
```
"Still dealing with dead batteries?","Anker PowerCore 20000mAh — Best pick for travelers","Never run out of power","Portable charger with 20000mAh capacity. As an Amazon Associate I earn from qualifying purchases. #ad","https://amazon.com/dp/XXX?tag=yourtag-20","2026-01-07_T1_PROD001.png","Smart Electronics Finds"
```

## Tips for Success

- **Test first**: Upload a small CSV with 2-3 rows to test
- **Check formatting**: Ensure quotes are properly escaped
- **Preview all**: Review every generated pin before downloading
- **Consistent branding**: Keep fonts and colors consistent across T1-T5
- **Mobile-friendly**: Remember pins are viewed on mobile devices
- **Readability**: Test at thumbnail size

## Troubleshooting

- **Placeholders not replacing**: Check exact spelling {{HOOK}} not {HOOK}
- **Text overflow**: Reduce font size or character limits
- **CSV errors**: Ensure proper quote escaping in CSV
- **Missing data**: Check all required columns are present

## Next Steps

After creating your templates:
1. Test Bulk Create with sample data
2. Adjust designs based on results
3. Save template links for easy access
4. Run your Python script to generate daily CSVs
5. Upload CSVs to Canva Bulk Create daily

