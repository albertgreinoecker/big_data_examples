from pdf2image import convert_from_path

pdf_path = "data/DA1.pdf"
output_dir = "/home/albert/tmp/seiten"

############################################
# # Seiten des PDFs in JPEG-Bilder umwandeln
############################################

# images = convert_from_path(
#     pdf_path,
#     dpi=300,          # Auflösung (300 für Druckqualität)
#     fmt="jpeg"
# )
#
# for i, image in enumerate(images, start=1):
#     image.save(f"{output_dir}/seite_{i:03}.jpg", "JPEG")
#     if i >= 10:
#         break
#
#


############################################
# # Wörter und deren Attribute aus einer bestimmten Seite extrahieren
############################################

# import pdfplumber
#
# with pdfplumber.open(pdf_path) as pdf:
#     page = pdf.pages[30]
#     words = page.extract_words(extra_attrs=[
#         "size", "fontname",
#         "x0", "x1", "top", "doctop",
#         "width", "height",
#         "upright"
#     ])

# for w in words:
#     print(w)


############################################
# # Bilder aus dem PDF extrahieren
############################################
import fitz #Das ist die PyMuPDF-Bibliothek
doc = fitz.open(pdf_path)

for page_no in range(len(doc)):
    page = doc[page_no]
    images = page.get_images(full=True) # Liste aller Bilder auf der Seite

    for idx, img_data in enumerate(images, start=1):
        xref = img_data[0]  # Abholen der Referenz des Bildes

        base_image = doc.extract_image(xref) # Bilddaten extrahieren
        img_bytes = base_image["image"]
        img_ext = base_image["ext"]

        width = base_image["width"]
        height = base_image["height"]
        colorspace = base_image["colorspace"]

        # Speichere das Bild
        img_path = output_dir  + f"/page_{page_no + 1:02d}_img_{idx:02d}.{img_ext}"
        with open(img_path, "wb") as f:
            f.write(img_bytes)