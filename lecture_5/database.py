from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL
DATABASE_URL = "sqlite:///./books.db"

# SQLAlchemy engine (connects Python to the database)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory for creating DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
