Bug Tracker Dashboard — Google Sheets-Based Implementation

Overview

This project is a lightweight bug tracking dashboard that allows manual entry of new bugs found each week. Rather than using a local database or cloud-hosted DB like RDS, this system leverages Google Sheets for persistent storage and visualization. The application offers a form interface for weekly submissions and a trend visualization using data pulled directly from the Google Sheet.

🔍 Why Google Sheets?

Cloud-native & easy to share

No server/database infrastructure required

Editable outside the app if needed

Compatible with automated charting (Chart.js, Plotly)

🛠️ Stack

Component

Technology

Backend

Python (Flask)

Storage

Google Sheets

Auth

Service Account JSON

Visualization

Chart.js (via HTML)

Deployment

Render (or local)

📋 Feature List

Manual weekly entry form: Week Ending, New Bugs, optional Notes

Append entry to Google Sheet

Line chart of new bugs per week

Optional: display notes as tooltips

🧱 Google Sheet Setup

Create a new Google Sheet (e.g. Weekly Bug Tracker)

Add the following headers in row 1:

Week Ending | New Bugs | Notes

Share the sheet with your Google Service Account:

Go to: https://console.cloud.google.com/iam-admin/serviceaccounts

Copy the service account email (e.g. feature-bot@project-id.iam.gserviceaccount.com)

Share the sheet with edit access

🧰 Step-by-Step Implementation

1. 📦 Set Up Flask Project

mkdir bug-tracker
cd bug-tracker
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install flask gspread oauth2client python-dotenv

2. 📄 Create .env File

GOOGLE_SHEET_ID=<your-sheet-id>
GOOGLE_SERVICE_ACCOUNT_JSON=credentials.json

3. 📁 Folder Structure

bug-tracker/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── chart.js (optional override)
├── .env
├── credentials.json

4. 🔑 Google Service Account

Follow instructions here: https://gspread.readthedocs.io/en/latest/oauth2.html

Download the JSON credentials file and save as credentials.json

5. ✍️ app.py Core Logic (Write + Read)

Flask route to submit weekly data

Flask route to read all data and return JSON for chart

6. 🖼️ HTML Interface

One page with:

Entry form (Week Ending, New Bugs, Notes)

Line chart (Chart.js) showing bug count trend

🔁 Deployment (Render)

Push project to GitHub

Create new Web Service in Render

Add environment variables in Render’s dashboard:

GOOGLE_SHEET_ID

GOOGLE_SERVICE_ACCOUNT_JSON (as a secret file or inline)

Set build command:

pip install -r requirements.txt

Set start command:

python app.py

✅ Future Enhancements

Email/Slack notifications for weekly input reminders

Spike annotations (notes shown inline)

Export to CSV

Access control

Let me know if you’d like the base code scaffolded next!

