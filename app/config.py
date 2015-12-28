import json

POSTGRES_USER = json.loads(open('app_secret.json',
                                'r').read())['postgres']['user']
postgres_pass = json.loads(open('app_secret.json',
                                'r').read())['postgres']['password']

APP_NAME = 'Last Week Rotten Trailers'
ERROR_401 = 'Unable to process information as requested'
APP_SECRET_KEY = 'Not a reel key'
SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
    str(POSTGRES_USER) + ':' + str(postgres_pass) + \
    '@localhost/last_week_rotten_trailers'

# CREATE ROLE postgres_user PASSWORD 'md5da14c899577a41fccbcdf41420c31e13'
# NOSUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
