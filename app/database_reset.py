from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
import json
import re
import uuid
import base64

import models
from models.movie_trailer_model import Base, MovieTrailerModel


with open(sys.argv[0]) as data_file:
    data = json.load(data_file)

for item in data:
    models.insert_to_trailer(item['id'], item['title'], item['year'],
                             item['rating'], item['runtime'],
                             item['release_date'], item['critics_score'],
                             item['audience_score'], item['synopsis'],
                             item['clips'])
print "done with movie trailers!!!"
