## Database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = ("postgresql://postgres:password@localhost/employee_db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# creates a base class that all our database models (tables) will inherit from.
Base = declarative_base()   
