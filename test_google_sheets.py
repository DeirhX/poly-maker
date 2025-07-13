#!/usr/bin/env python3
"""
Test script to verify Google Sheets integration is working properly.
Run this after setting up your credentials.json and .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_google_sheets():
    """Test if Google Sheets integration is working."""
    print("🧪 Testing Google Sheets Integration...")
    
    # Check if required files exist
    if not os.path.exists('credentials.json'):
        print("❌ credentials.json not found in main directory")
        return False
    
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        return False
    
    # Check if SPREADSHEET_URL is set
    spreadsheet_url = os.getenv("SPREADSHEET_URL")
    if not spreadsheet_url:
        print("❌ SPREADSHEET_URL not set in .env file")
        return False
    
    print(f"✅ Found SPREADSHEET_URL: {spreadsheet_url}")
    
    # Try to import and use the Google utils
    try:
        from poly_utils.google_utils import get_spreadsheet
        print("✅ Successfully imported Google utilities")
        
        # Test connection
        spreadsheet = get_spreadsheet()
        print("✅ Successfully connected to Google Sheets")
        
        # Check if it's a read-only or full access spreadsheet
        try:
            # Try full access spreadsheet first
            worksheets = spreadsheet.worksheets()
            print(f"✅ Found {len(worksheets)} worksheets:")
            for ws in worksheets:
                print(f"   - {ws.title}")
        except AttributeError:
            # Read-only spreadsheet - try to access a common worksheet
            print("✅ Using read-only mode")
            try:
                # Try to access common worksheet names
                test_worksheet = spreadsheet.worksheet("Sheet1")
                print("✅ Successfully accessed Sheet1")
            except Exception as e:
                print(f"⚠️  Could not access default worksheet: {e}")
                print("   This is normal if your sheet has different worksheet names")
        
        return True
        
    except Exception as e:
        print(f"❌ Error connecting to Google Sheets: {e}")
        return False

if __name__ == "__main__":
    success = test_google_sheets()
    if success:
        print("\n🎉 Google Sheets integration is working correctly!")
    else:
        print("\n❌ Google Sheets integration needs to be fixed.")
        print("\nMake sure you have:")
        print("1. Downloaded Google Service Account JSON file")
        print("2. Renamed it to 'credentials.json' in main directory")
        print("3. Copied the sample Google Sheet")
        print("4. Shared the sheet with your service account email")
        print("5. Updated SPREADSHEET_URL in .env file") 