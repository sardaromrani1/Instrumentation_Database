from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database engine (SQLite in this example)
engine = create_engine("sqlite:///instrumentation_database.db", echo=True)

# Base class for models
Base = declarative_base()

# Define the Instrument model
class Instrument(Base):
    __tablename__ = "instruments"

    id = Column(Integer, primary_key= True, autoincrement= True)
    device_name = Column(String, nullable= False)
    manufacturer = Column(String, nullable= False)
    model = Column(String, nullable= False)
    part_number = Column(String, nullable= False)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind= engine)
session = Session()
