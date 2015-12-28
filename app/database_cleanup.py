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

rows = models.delete_movie_trailers()

print("%d rows were deleted from table", rows)
