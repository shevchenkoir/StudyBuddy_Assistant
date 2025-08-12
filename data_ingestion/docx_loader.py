import docx2txt

def extract_text_from_docx(filepath):
    return docx2txt.process(filepath)