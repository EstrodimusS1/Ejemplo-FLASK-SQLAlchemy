from src.config import db
from sqlalchemy import Column, Integer, String

class Book(db.Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer)