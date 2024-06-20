import fitz
from .process_text import extract_relevant_info
from .insert_data import insert_data

def load_data(pdf_path, pages):
    doc = fitz.open(pdf_path)
    for page_num in pages:
        page = doc.load_page(page_num)
        text = page.get_text("text")
        processed_text = extract_relevant_info(text)
        insert_data(page_num, processed_text)
    doc.close()

# Konfigurace pro načítání stranek 80 až 97
if __name__ == "__main__":
    pdf_path = "path_to_shadowrun_rules.pdf"
    pages = list(range(80, 98))  # Stránky 80 až 97
    load_data(pdf_path, pages)
