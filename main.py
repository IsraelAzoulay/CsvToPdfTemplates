# Third program - Pdf Generation.

# Third party library for creating pdf objects instances of the FPDF class.
from fpdf import FPDF
import pandas as pd


# Creating the pdf object instance.
pdf = FPDF(orientation="portrait", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Creating the pdf page with the "add_page()" func which adds page to the
    # document and belongs to the FPDF class.
    pdf.add_page()
    # Setting the font styles properties of a generic cell's content.
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # Creating a single cell.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    pdf.line(10, 21, 200, 21)

# Generating the pdf file on the disk.
pdf.output("output.pdf")