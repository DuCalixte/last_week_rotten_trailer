import os
import sys
import json
import re
import uuid
import base64
from datetime import date, datetime
import traceback
import subprocess
from functools import wraps


from movie_trailer_model import Base, MovieTrailerModel

from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import sessionmaker, outerjoin
from flask import Flask, g, jsonify, abort

from app import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.bind = engine
Base.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()


def commit_and_close(f):
    @wraps(f)
    def session_functions(*args, **kwargs):
        session = DBsession()
        res = f(*args, **kwargs)
        session.close()
        return res
    return session_functions


@commit_and_close
def insert_to_trailer(id, title, year, rating, runtime, release_date,
                      critics_score, audience_score, synopsis, clips):
    movie_trailer = MovieTrailerModel(id=id, title=title, year=year,
                                      rating=rating, runtime=runtime,
                                      release_date=release_date,
                                      critics_score=critics_score,
                                      audience_score=audience_score,
                                      synopsis=synopsis, clips=clips)
    session.add(movie_trailer)
    session.commit()
    session.refresh(movie_trailer)
    return movie_trailer


@commit_and_close
def select_movie_by_id(id):
    return session.query(MovieTrailerModel).filter_by(id=id).scalar()


@commit_and_close
def select_all_movies():
    return session.query(MovieTrailerModel).all()


@commit_and_close
def delete_item(itemToDelete):
    session.delete(itemToDelete)
    session.commit()


@commit_and_close
def delete_movie_trailers():
    try:
        rows = session.query(MovieTrailerModel).delete()
        session.commit()
        return rows
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(404)


@commit_and_close
def update_item(item, title, rating, critics_score, audience_score, synopsis,
                clips):
    item.title = title
    item.rating = rating
    item.critics_score = critics_score
    item.audience_score = audience_score
    item.synopsis = synopsis
    item.clips = clips
    item.updated_time = datetime.now()
    session.commit()
