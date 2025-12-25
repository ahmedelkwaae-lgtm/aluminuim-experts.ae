import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

pdf_path = "❖  A L U M I N I U M   E X P E R T S  ❖.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)