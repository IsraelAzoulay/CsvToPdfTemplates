# Third program - Pdf Generation.

# Third party library for creating pdf objects instances of the FPDF class.
from fpdf import FPDF
import pandas as pd


# Creating the pdf object instance. (All the numbers in the styles below except the
# ones of the size will be in mm - milimiter
pdf = FPDF(orientation="portrait", unit="mm", format="A4")
# Canceling the auto page break func.
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Creating\adding a "master" pdf page (with the "add_page()" func which adds page
    # to the document and belongs to the FPDF class).
    pdf.add_page()

    # Setting the font styles properties of a generic cell's content.
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # Creating a single cell.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Creating and setting the footer.
    # "ln()" is a break line func.
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for page in range(row["Pages"] - 1):
        pdf.add_page()

        # Creating and setting the footer.
        # "ln()" is a break line func.
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Generating the pdf file on the disk.
pdf.output("output.pdf")