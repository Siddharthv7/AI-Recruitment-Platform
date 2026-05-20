from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)

    email = Column(String, unique=True, index=True)

    password = Column(String)

class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    skills = Column(String)

    resume_score = Column(Integer)