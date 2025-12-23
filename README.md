# BookletBuilder

BookletBuilder is a Python tool that generates a PDF booklet from data stored in a Google Sheet, using a LaTeX template.

## Features

- Fetches data from a Google Sheet using a service account.
- Populates a customizable LaTeX template with your data.
- Compiles the LaTeX to a PDF, one page per entry.
- Handles special characters and URLs in abstracts.

## Installation

1. **Clone this repository:**

   ```sh
   git clone https://github.com/yourusername/BookletBuilder.git
   cd BookletBuilder
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Install a LaTeX distribution:**

   - On Mac, install [MacTeX](https://tug.org/mactex/).
   - Ensure `pdflatex` is available in your terminal.

## Configuration

1. **Google Cloud Setup:**

   - Create a Google Cloud project.
   - Enable the **Google Sheets API** and **Google Drive API**.
   - Create a **service account** and download the `credentials.json` file.
   - Place `credentials.json` in the `src/` directory.
   - Share your Google Sheet with the service account email.

2. **Set your Spreadsheet ID:**

   - Create a `.env` file in the project root:
     ```
     SPREADSHEET_ID=your_actual_spreadsheet_id_here
     ```
   - **Do not commit `.env` or `credentials.json` to version control.**

3. **Adjust the data range in `src/main.py` if needed:**
   ```python
   range_name = "A1:J100"  # Adjust as needed
   ```

## Usage

Run the main script:

```sh
python src/main.py
```

- The output PDF and intermediate files will be generated in the `output/` directory.

## Customization

- Edit `src/latex_template.tex` to change the layout or formatting of the generated booklet.
- Adjust the data mapping in `src/main.py` if your sheet structure changes.

## Security

- Your credentials and spreadsheet ID are kept out of version control via `.gitignore`.
- **Never share your `credentials.json` or `.env` file.**

## License
[Creative Commons Zero v1.0 Universal](LICENSE)
