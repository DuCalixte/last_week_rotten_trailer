'''
This page module simply loads the data for the app as json endpoints.
    The module contents only respond to get requests.
'''
import os
import sys
import json
import random
import string
import re

from flask import Blueprint, render_template, redirect, url_for, \
    request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from app import utilities

import app.models as models
from app.models import movie_trailer_model as data_models
from app.models.movie_trailer_model import Base, MovieTrailerModel

module = Blueprint('json_endpoints', __name__)


@module.route('/movies/', methods=['GET'])
@module.route('/movies/json', methods=['GET'])
def show_all_movies():
    try:
        movies = models.select_all_movies()
        if movies is None:
            abort(403)
        else:
            return jsonify(movies=[r.serialize for r in movies])
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)
