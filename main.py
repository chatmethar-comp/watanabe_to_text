import pdfplumber
import os

# Directory containing the PDF files
input_directory = 'data/N3K4/'
output_file_path = 'output/N3K4/output.txt'

# Function to extract text from a PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Open the output file in write mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Loop through all files in the directory
    for filename in os.listdir(input_directory):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_directory, filename)
            print(f"Processing {pdf_path}...")
            # Extract text from the PDF and write it to the output file
            extracted_text = extract_text_from_pdf(pdf_path)
            output_file.write(f"=== {filename} ===\n")
            output_file.write(extracted_text + "\n\n")
            print(f"Finished processing {filename}")

print(f"All PDF files have been processed and saved to {output_file_path}.")
