import os
from datetime import timedelta

DEBUG = os.getenv("FLASK_DEBUG")
TITLE = "Anunbis"
SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
JSON_AS_ASCII = False
JWT_ACCESS_TOKEN_EXPIRES = os.getenv(
    "FLASK_JWT_ACCESS_TOKEN_EXPIRES", timedelta(hours=1))
