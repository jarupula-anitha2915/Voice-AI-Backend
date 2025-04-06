import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

def log_to_google_sheets(session_id, user_msg, bot_response):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Voice AI Logs").sheet1
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([session_id, user_msg, bot_response, now])