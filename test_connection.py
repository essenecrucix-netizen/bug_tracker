import os
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# Load environment variables
load_dotenv()

# Set up Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"), scope
)
client = gspread.authorize(creds)

# Access the sheet
sheet_id = os.getenv("GOOGLE_SHEET_ID")
sheet = client.open_by_key(sheet_id).sheet1

# Append test row
today = date.today().isoformat()
sheet.append_row([today, 99, "✅ Test bug entry from Python"])

print(f"✅ Success! Test row added for {today}")