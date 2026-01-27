from pdf2image import convert_from_path

pdf_path = "data/DA1.pdf"
output_dir = "/home/albert/tmp/seiten"

############################################
# # Seiten des PDFs in JPEG-Bilder umwandeln
############################################

images = convert_from_path(
    pdf_path,
    dpi=300,          # Auflösung (300 für Druckqualität)
    fmt="jpeg"
)

for i, image in enumerate(images, start=1):
    image.save(f"{output_dir}/seite_{i:03}.jpg", "JPEG")
    if i >= 10:
        break




############################################
# # Wörter und deren Attribute aus einer bestimmten Seite extrahieren
# Liefert leider nur die Buchstaben, nicht die zusammengesetzten Wörter!!!!!!!!!!!!!!!!!!!!!
############################################


# import pdfplumber
#
# with pdfplumber.open(pdf_path) as pdf:
#     page = pdf.pages[30]
#     words = page.extract_words(
#         extra_attrs=[
#         "size", "fontname",
#         "x0", "x1", "top", "doctop",
#         "width", "height",
#         "upright"
#     ])
#
# for w in words:
#     print(w['text'])
#
# chars = page.chars
#
# current = []
# words = []
#
# for c in chars:
#     if current and c["x0"] - current[-1]["x1"] > 0.1:
#         words.append("".join(ch["text"] for ch in current))
#         current = []
#     current.append(c)
#
# print(words)
#
# if current:
#     words.append("".join(ch["text"] for ch in current))
# text = page.extract_text()
#print(text)

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



for page_number, page in enumerate(doc):
    #words = page.get_text("words")
    # Format: (x0, y0, x1, y1, "Wort", block_no, line_no, word_no)

    #for w in words:
    #    x0, y0, x1, y1, text, block, line, word = w
    #    print(page_number, text)


    #print(page.get_text("blocks"))

    print(f"--- Seite {page_number + 1} ---")
    print(".............................")
    data = page.get_text("dict")

    for block in data["blocks"]:
        if block["type"] == 0:  # Textblock
            for line in block["lines"]:
                for span in line["spans"]: #Ein Span ist ein zusammenhängender Textbereich mit exakt gleichen Texteigenschaften
                    print(
                        span["text"],
                        span["bbox"]  # (x0, y0, x1, y1)
                    )

