from docling.document_converter import DocumentConverter
import pandas as pd
import os


def extract_tables_from_scanned_pdf(file_path):
    print(f"Processing: {file_path}...")

    # Initialize the converter (handles OCR and TableFormer vision models automatically)
    converter = DocumentConverter()

    # Run the AI pipeline on the PDF
    result = converter.convert(file_path)

    tables = result.document.tables

    if not tables:
        print("No tables detected in the document.")
        return

    print(f"Found {len(tables)} table(s).")

    # Extract each table and convert to a Pandas DataFrame
    for i, table in enumerate(tables):
        df = table.export_to_dataframe()

        print(f"\n--- Table {i + 1} Preview ---")
        print(df.head())  # Print the first few rows to check performance

        # Save to CSV for manual inspection
        output_filename = f"extracted_table_{i + 1}.csv"
        df.to_csv(output_filename, index=False)
        print(f"Saved to: {output_filename}")


# --- Execution ---
# Replace with the path to your scanned PDF
my_pdf_path = "sample-report.pdf"

if os.path.exists(my_pdf_path):
    extract_tables_from_scanned_pdf(my_pdf_path)
else:
    print("Please update the 'my_pdf_path' variable with a valid file path.")