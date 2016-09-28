from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    author = Column(String(120), unique=False)
    isbn = Column(Integer, unique=False)
    status = Column(String(120), unique=False)

    def __init__(self, title=None, author=None, isbn=None, status=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __repr__(self):
        return 'Title: %r' % (self.title)
