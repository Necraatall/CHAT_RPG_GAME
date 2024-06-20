from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .item import Item
from .extracted_text import ExtractedText
from .character import Character
