import fitz

input_file = "Endline.pdf"
output_file = "output.txt"

doc = fitz.open(input_file)

out = open(output_file, "wb")
for page in doc:
    text = page.get_text().encode("utf8")
    out.write(text)
    out.write(bytes((12,)))
out.close()

"""
new_input = "output.txt"
new_output = "stringmanipulation.txt"
"""
"""





"""

# for pi in range(len(doc)):
#     page = doc[pi]
#     il = page.get_images()

#     if il:
#         print(f"found {len(il)} images on page {pi}")
#     else:
#         print("no images found on", pi)
#     for imgi, img in enumerate(il, start=1):
#         ref = img[0]
#         pix = fitz.Pixmap(doc, ref)

#         if pix.n - pix.alpha > 3:
#             pix = fitz.Pixmap(fitz.csRGB, pix)

#         pix.save("page_%s-image_%s.png" % (pi, imgi))
#         pix = None
