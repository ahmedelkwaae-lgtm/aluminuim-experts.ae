import fitz  # PyMuPDF
import os

pdf_path = "❖  A L U M I N I U M   E X P E R T S  ❖.pdf"
output_folder = "assets/images/extracted"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    images = page.get_images(full=True)
    
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_name = f"page_{page_num+1}_img_{img_index+1}.{image_ext}"
        image_path = os.path.join(output_folder, image_name)
        
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)
        
        print(f"Saved {image_path}")

doc.close()