from pypdf import PdfReader, PdfWriter
from pathlib import Path


def remove_pdf_password(input_file, output_file, password):
    input_path = Path(input_file)
    output_path = Path(output_file)

    # Check whether input file exists
    if not input_path.exists():
        return False, "Input file not found."

    try:
        reader = PdfReader(input_path)

        # Check if PDF is password protected
        if reader.is_encrypted:
            if not reader.decrypt(password):
                return False, "Incorrect password."

        writer = PdfWriter()

        # Copy all pages to the new PDF
        for page in reader.pages:
            writer.add_page(page)

        # Save the new PDF without encryption
        with open(output_path, "wb") as output:
            writer.write(output)

        return True, "Password protection removed successfully."

    except Exception as e:
        return False, f"Error: {e}"