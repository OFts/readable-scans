import os
import img2pdf

# https://image2pdf.iblogbox.com/

# images[0].save(pdf_file, "PDF" ,resolution=100.0, save_all=True, append_images=images)
dirname = "C:/Users/oscar/Development/Sandbox/SkimageTest/local/"
imgs = []
for fname in os.listdir(dirname):
	if not fname.endswith(".png"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open("name.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))