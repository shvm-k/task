import fitz  # PyMuPDF for PDF parsing

def extract_text_from_pdf(pdf_path):
    """Extracts text from the given PDF file."""
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
        return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text: {e}")

