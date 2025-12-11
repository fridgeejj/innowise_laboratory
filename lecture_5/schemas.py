from pydantic import BaseModel

# Base schema shared by other schemas
class BookBase(BaseModel):
    title: str
    author: str
    year: int | None = None

# Schema for creating a new book
class BookCreate(BookBase):
    pass

# Schema for updating an existing book (all fields optional)
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None

# Schema for returning a book in API responses
class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True   # Enables reading ORM objects
