from sqlalchemy import create_engine, Column, Integer, VARCHAR, Sequence, Date,DECIMAL, ForeignKey
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base # A base class for all classes definitions
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Create an engine
engine = create_engine("postgresql://postgres:postgres@localhost:5432/movies_db", echo=False)

# create a configured 'session' class
Session = sessionmaker(bind=engine)
session =  Session()

Base = declarative_base()

class  Movie(Base):
    __tablename__ = "Movies"

    movie_id = Column(VARCHAR(50), primary_key=True)
    title = Column(VARCHAR(100))
    image_url = Column(VARCHAR(200))
    serie_type = Column(VARCHAR(50))
    rank = Column(Integer)
    casts = Column(VARCHAR(200))
    year = Column(Integer)




Base.metadata.create_all(engine)