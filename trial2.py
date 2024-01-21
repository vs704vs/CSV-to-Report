from fpdf import FPDF
import streamlit as st
from zipfile import *

def create_pdf():
    pdf1 = FPDF()
    pdf1.add_page()
    pdf1.set_font("Helvetica", size=15)
    pdf1.cell(200, 10, text="Hello World 1!", ln=1)
    pdf1.output("files/output1.pdf")

    pdf2 = FPDF()
    pdf2.add_page()
    pdf2.set_font("Helvetica", size=15)
    pdf2.cell(200, 10, text="Hello World 2!", ln=1)
    pdf2.output("files/output2.pdf")

create_pdf()

with ZipFile('files/compress.zip', mode='w', compression=ZIP_DEFLATED) as zip_file_object:
    for j in range(2):
        zip_file_object.write("files/output" + str(j+1) + ".pdf")

with open("files/compress.zip", "rb") as f:
    zip_bytes = f.read()
    st.download_button(
        label="Download ZIP",
        data=zip_bytes,
        file_name="compress.zip",
        mime="application/zip"
    )
