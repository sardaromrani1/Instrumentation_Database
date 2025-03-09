from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database (SQLite in this example)
DATABASE_URL = "sqlite:///instrumentation.db"   # Change this for PostgreSQL or MySQL

# Create a database engine ( SQLite in this example )
engine = create_engine(DATABASE_URL, echo=True)

# Base class for SQLAlchemy models
Base = declarative_base()

# Define Instrumentation Table
class Instrumentation(Base):
    __tablename__ = "instrumentation"

    id = Column(Integer, primary_key=True, autoincrement= True)
    device_name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    model = Column(String, nullable=False)
    part_number = Column(String, nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(bind= engine)
session= SessionLocal()

        

