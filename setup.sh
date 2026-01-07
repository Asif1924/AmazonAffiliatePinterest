#!/bin/bash

# Amazon Affiliate Pinterest Automation - Setup Script
# This script helps you set up the project quickly

echo "=========================================="
echo "Amazon Affiliate Pinterest Automation"
echo "Setup Script"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping."
else
    python3 -m venv venv
    echo "Virtual environment created."
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

# Create config file if it doesn't exist
if [ ! -f "config.py" ]; then
    echo "Creating config.py from template..."
    cp config.example.py config.py
    echo "✓ config.py created. Please edit it with your settings."
else
    echo "config.py already exists. Skipping."
fi
echo ""

# Make shell scripts executable
echo "Making shell scripts executable..."
chmod +x run_daily_csv.sh
chmod +x setup.sh
echo "✓ Scripts are now executable"
echo ""

# Create necessary directories
echo "Creating directories..."
mkdir -p credentials
mkdir -p daily_csv
mkdir -p logs
echo "✓ Directories created"
echo ""

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Set up your Google Sheet (see docs/GOOGLE_SHEETS_SETUP.md)"
echo "2. Get Google Service Account credentials"
echo "3. Save credentials to: credentials/google_service_account.json"
echo "4. Edit config.py with your settings:"
echo "   - GOOGLE_SHEET_ID"
echo "   - LLM_PROVIDER and API key"
echo "5. Test the script: python3 daily_canva_csv.py"
echo "6. Set up Canva templates (see docs/CANVA_TEMPLATE_SETUP.md)"
echo "7. Schedule daily execution (see docs/SCHEDULING.md)"
echo ""
echo "For detailed instructions, see README.md"
echo ""

