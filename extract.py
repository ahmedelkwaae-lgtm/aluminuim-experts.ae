import PyPDF2

pdf_path = r'c:\Users\Moamen\OneDrive\Desktop\❖ A L U M I N I U M E X P E R T S ❖.pdf'

with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    print(text)