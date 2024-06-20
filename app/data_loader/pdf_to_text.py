import fitz

def extract_text_from_pages(pdf_path, page_numbers):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in page_numbers:
        page = doc.load_page(page_num)
        text += page.get_text()
    return text
