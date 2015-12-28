import os
import sys
import json
import string
import random
import hashlib
import requests
import urllib
import jinja2
import traceback
from flask import Flask, Blueprint, current_app, Response, request, abort, \
    render_template, make_response, flash, redirect, url_for
from werkzeug import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps
import webapp2

# Loading login session library
from flask import session as login_session
from app import utilities

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.secret_key = utilities.random_state()

from app import views
from app.views import page
from app.views import json_endpoints

from app import models
from app.models import movie_trailer_model
from app.models.movie_trailer_model import Base, MovieTrailerModel

app.register_blueprint(page.module)
app.register_blueprint(json_endpoints.module)
app.register_blueprint(movie_trailer_model.data)
