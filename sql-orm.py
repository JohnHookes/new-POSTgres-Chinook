from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the chinook database
db - create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class based model for the "Artist" table
class Album(base):
    __tablename__ = "Album"
    AlbumId


# instead of connecting to the database difrectly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#opens an actual session by calling the session() subclass defined above
session = Session()

# creating the database using declarative base subclass
base.metadata.create_all(db)






