from ..database import SessionLocal
from ..models import ExtractedText

def insert_data(page_number, text_list):
    db = SessionLocal()
    for text in text_list:
        extracted_text = ExtractedText(page_number=page_number, text=text)
        db.add(extracted_text)
    db.commit()
