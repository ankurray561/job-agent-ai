from PyPDF2 import PdfReader

def extract_cv_text():
    reader = PdfReader("ANKUR_RAY_CV_2026.pdf")
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()