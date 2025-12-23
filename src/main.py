from google_sheets import get_sheet_data
from utils import render_latex_template, compile_latex_to_pdf
from dotenv import load_dotenv
import os
import re

def replace_urls_with_footnotes(text):
    url_pattern = r'(https?://[^\s]+)'
    def replacer(match):
        url = match.group(0)
        return r'\footnote{\url{' + url + '}}'
    return re.sub(url_pattern, replacer, text)

def main():
    # Replace with your actual spreadsheet ID and range
    load_dotenv()
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    range_name = "A1:J54"  # Adjust as needed

    raw_data = get_sheet_data(spreadsheet_id, range_name)
    raw_data = raw_data[1:]  # Skip header

    # Map columns to field names
    data = []
    for row in raw_data:
        row += [''] * (10 - len(row))
        abstract = row[8]
        abstract_with_footnotes = replace_urls_with_footnotes(abstract)
        entry = {
            "lastname": row[0],
            "firstname": row[1],
            "title": row[2],
            "email": row[3],
            "affiliation": row[5],
            "format": row[7],
            "abstract": abstract_with_footnotes,
            "coauthors": row[9],
            }
        data.append(entry)
    
    tex_path = render_latex_template(data, output_dir="output")
    compile_latex_to_pdf(tex_path, output_dir="output")


if __name__ == "__main__":
    main()

