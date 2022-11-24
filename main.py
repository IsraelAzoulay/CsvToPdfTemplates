# Third program - Pdf Generation.

# Third party library for creating pdf objects instances of the FPDF class.
from fpdf import FPDF
import pandas as pd


# Creating the pdf object instance. (All the numbers in the styles below except the
# ones of the size will be in mm - milimiter). Besides, canceling the auto page break func.
pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Creating\adding a "master" pdf page (with the "add_page()" func which adds page
    # to the document and belongs to the FPDF class).
    pdf.add_page()

    # Creating and setting the header: font, color, cell and the line underneath.
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Creating empty lines from header to footer.
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Creating and setting the footer: Breaking lines from the header - "ln()" func,
    # font, color and cell.
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for page in range(row["Pages"] - 1):
        pdf.add_page()

        # Creating and setting the footer: break lines, font, color and cell.
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Creating empty lines from header to footer.
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

# Generating the pdf file on the disk.
pdf.output("output.pdf")