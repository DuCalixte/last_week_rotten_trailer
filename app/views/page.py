'''
This page module simply loads the app
'''
import os
import sys
from flask import Flask, render_template, send_from_directory
from flask import Blueprint, render_template, session, redirect, url_for, \
    request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

app = Flask('app')
module = Blueprint('page', __name__, static_folder='static')


@module.route('/')
@module.route('/index')
def index():
    return render_template('index.html')


@module.route('/favicon.ico')
def favicon():
    try:
        return send_from_directory(os.path.join(app.root_path,
                                                'static', 'img', 'fav'),
                                   '164_Tomato.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)
