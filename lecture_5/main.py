from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, SessionLocal
import models
import schemas

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Dependency: provides a database session to each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------
# POST /books/ — Add a new book to the database
# ---------------------------------------------------------
@app.post("/books/", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())  # Convert Pydantic model to ORM model
    db.add(db_book)
    db.commit()
    db.refresh(db_book)  # Refresh to get the generated ID
    return db_book


# ---------------------------------------------------------
# GET /books/ — Retrieve all books
# ---------------------------------------------------------
@app.get("/books/", response_model=List[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


# ---------------------------------------------------------
# DELETE /books/{book_id} — Remove a book by ID
# ---------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


# ---------------------------------------------------------
# PUT /books/{book_id} — Update an existing book
# ---------------------------------------------------------
@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, updates: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Only update fields that were provided
    update_data = updates.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


# ---------------------------------------------------------
# GET /books/search/?title=... — Search books by title
# ---------------------------------------------------------
@app.get("/books/search/", response_model=List[schemas.BookOut])
def search_books(title: str, db: Session = Depends(get_db)):
    # Case-insensitive substring search
    return db.query(models.Book).filter(models.Book.title.contains(title)).all()
