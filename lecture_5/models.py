from sqlalchemy import Column, Integer, String
from database import Base

# ORM model representing a "books" table in the database
class Book(Base):
    __tablename__ = "books"

    # Unique identifier for each book
    id = Column(Integer, primary_key=True, index=True)

    # Book title (required)
    title = Column(String, nullable=False)

    # Book author (required)
    author = Column(String, nullable=False)

    # Publication year (optional)
    year = Column(Integer, nullable=True)
