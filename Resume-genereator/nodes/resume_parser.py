from schemas import ResumeClass
import pdfplumber

def Resume_Parser_node(state:ResumeClass):
    path = state['Old_Resume']
    if not path.lower().endswith('.pdf'):
        raise ValueError("Unsupported file format. Please provide a PDF file.")
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return {'Old_full_resume': text}