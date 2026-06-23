# Create User Table

from sqlalchemy import Column, Integer, String
from database import Base
from database import engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)



