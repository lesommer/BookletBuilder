from google_sheets import get_sheet_data
from utils import render_latex_template, compile_latex_to_pdf

def main():
    # Replace with your actual spreadsheet ID and range
    #spreadsheet_id = "1rSoqATkoUgQCZajLit5NaYQDYWqAI7PU"
    spreadsheet_id = "1VtECwsqz2YzUCluN9obU7-2qIpna_MFM3XmWm-jmzuo"
    range_name = "A1:J54"  # Adjust as needed

    raw_data = get_sheet_data(spreadsheet_id, range_name)
    raw_data = raw_data[1:]  # Skip header

    # Map columns to field names
    data = []
    for row in raw_data:
        # Ensure row has enough columns
        row += [''] * (10 - len(row))
        entry = {
            "lastname": row[0],
            "firstname": row[1],
            "title": row[2],
            "email": row[3],
            "affiliation": row[5],
            "format": row[7],
            "abstract": row[8],
            "coauthors": row[9],
        }
        data.append(entry)

    tex_path = render_latex_template(data, output_dir="output")
    compile_latex_to_pdf(tex_path, output_dir="output")


if __name__ == "__main__":
    main()

