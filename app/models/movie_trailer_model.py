'''
    Introducing data models utilized in this app:
        Base, MovieTrailerModel
'''
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, func
from flask import Blueprint

data = Blueprint('movie_trailers', __name__)

# from database_setup import Base
Base = declarative_base()


# Crating table model
class MovieTrailerModel(Base):
    __tablename__ = "movie_trailers"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    year = Column(Integer, nullable=False)
    mpaa_rating = Column(String(8), nullable=False)
    runtime = Column(Integer, nullable=False)
    release_date = Column(DateTime, nullable=False)
    critics_score = Column(Integer, nullable=True)
    audience_score = Column(Integer, nullable=True)
    synopsis = Column(String(1024), nullable=False)
    clips = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.updated_at is None:
            self.updated_at = self.created_at
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'rating': self.mpaa_rating,
            'runtime': self.runtime,
            'release_date': self.release_date,
            'critics_score': self.critics_score,
            'audience_score': self.audience_score,
            'synopsis': self.synopsis,
            'clips': self.clips,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
