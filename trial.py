from fpdf import FPDF
import streamlit as st

def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Hello World!", ln=1)
    pdf.output("output.pdf")

create_pdf()

with open("output.pdf", "rb") as f:
    pdf_bytes = f.read()
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="output.pdf",
        mime="application/pdf"
    )
