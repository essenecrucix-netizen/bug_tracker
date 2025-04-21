from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"), scope
)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        week_ending = request.form["week_ending"]
        new_bugs = request.form["new_bugs"]
        notes = request.form.get("notes", "")

        sheet.append_row([week_ending, new_bugs, notes])
        return redirect("/")

    records = sheet.get_all_records()
    return render_template("index.html", records=records)

@app.route("/chart-data")
def chart_data():
    records = sheet.get_all_records()
    labels = [r["Week Ending"] for r in records]
    data = [int(r["New Bugs"]) for r in records]
    return {"labels": labels, "data": data}

if __name__ == "__main__":
    app.run(debug=True)