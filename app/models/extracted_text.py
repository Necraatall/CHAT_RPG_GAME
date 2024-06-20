from sqlalchemy import Column, Integer, Text
from . import Base

class ExtractedText(Base):
    __tablename__ = "extracted_text"
    
    id = Column(Integer, primary_key=True, index=True)
    page_number = Column(Integer, index=True)
    text = Column(Text, index=True)
