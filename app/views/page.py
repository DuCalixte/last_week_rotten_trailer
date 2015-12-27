'''
This page module simply loads the app
'''
import os
import sys
from flask import Flask, render_template, send_from_directory
from flask import current_app, Blueprint, render_template, session, redirect, url_for, \
    request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

from app import utilities
print app

module = Blueprint('page', __name__)


@module.route('/')
@module.route('/index')
def index():
    return render_template('index.html')


@module.route('/favicon.ico')
def favicon():
    try:
        print ("---------------------------------------")
        print ('os path', os.path)
        #print ('app: ', app)
        #print ('app path:', app.root_path)
        #print (os.path.join(app.root_path))
        print ("---------------------------------------")
        #print ('finally:', send_from_directory(os.path.join(app.root_path, 'static')))

        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'img/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')
        #return send_from_directory(os.path.join(app.root_path, 'static/icons/ico/favicon.ico'))
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)

