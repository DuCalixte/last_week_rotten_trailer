#!/bin/sh

virtualenv venv
. venv/bin/activate

pip install flask
pip install webob
pip install webapp2
pip install psycopg2
pip install Flask-SQLAlchemy
pip install Flask-Migrate
