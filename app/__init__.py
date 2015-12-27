import os
import sys
import json
import string
import random
from flask import Flask, Blueprint, current_app, Response, request, abort, render_template, make_response, flash, redirect, url_for
import hashlib
import requests
import urllib
import jinja2
import traceback
from werkzeug import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps
import webapp2

# Loading login session library
from flask import session as login_session

app = Flask(__name__)

app.config.from_pyfile("config.py")
from app import utilities

from app import views
from app.views import page
app.register_blueprint(page.module)

app.secret_key = utilities.random_state()
