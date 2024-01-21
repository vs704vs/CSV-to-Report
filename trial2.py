from fpdf import FPDF
import streamlit as st
from zipfile import *

# Function to create two PDFs with different content
def create_pdf():
    # Create the first PDF
    pdf1 = FPDF()
    pdf1.add_page()
    pdf1.set_font("Helvetica", size=15)
    pdf1.cell(200, 10, text="Hello World 1!", ln=1)
    pdf1.output("files/output1.pdf")

    # Create the second PDF
    pdf2 = FPDF()
    pdf2.add_page()
    pdf2.set_font("Helvetica", size=15)
    pdf2.cell(200, 10, text="Hello World 2!", ln=1)
    pdf2.output("files/output2.pdf")

# Call the function to create PDFs
create_pdf()

# Create a ZIP file containing the two PDFs
with ZipFile('files/compress.zip', mode='w', compression=ZIP_DEFLATED) as zip_file_object:
    for j in range(2):
        zip_file_object.write("files/output" + str(j+1) + ".pdf")

# Read the ZIP file as bytes
with open("files/compress.zip", "rb") as f:
    zip_bytes = f.read()

# Create a Streamlit download button for the ZIP file
st.download_button(
    label="Download ZIP",
    data=zip_bytes,
    file_name="compress.zip",
    mime="application/zip"
)
