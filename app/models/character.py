from sqlalchemy import Column, Integer, String
from . import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    health = Column(Integer)
    money = Column(Integer)
    race = Column(String)
    class_type = Column(String)
