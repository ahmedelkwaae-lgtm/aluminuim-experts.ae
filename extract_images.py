from pdf2image import convert_from_path
import os

pdf_path = "❖  A L U M I N I U M   E X P E R T S  ❖.pdf"
output_folder = "assets/images/extracted"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

images = convert_from_path(pdf_path)

for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"page_{i+1}.png")
    image.save(image_path, 'PNG')
    print(f"Saved {image_path}")