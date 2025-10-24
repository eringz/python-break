import img2pdf

# Single image to PDF
with open("ALS BLDG - 1F.pdf", "wb") as f:
    f.write(img2pdf.convert("ALS BLDG - 1F.jpg"))
