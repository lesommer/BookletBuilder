import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet_data(spreadsheet_id, range_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("src/credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(spreadsheet_id)
    worksheet = sheet.sheet1  # or use .worksheet('SheetName')
    data = worksheet.get(range_name)
    return data

