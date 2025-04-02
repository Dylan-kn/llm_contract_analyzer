import os 
import pdfplumber
import docx

def extract_text_from_file(file):
    filename = file.name.lower()

    if filename.endswith('.pdf'):
        return extract_pdf(file)
    elif filename.endswith('.docx'):
        return extract_docx(file)
    elif filename.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        return "File type not supported"
    
def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        return text
    
def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
