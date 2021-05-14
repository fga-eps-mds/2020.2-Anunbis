import os
from datetime import timedelta

DEBUG = os.getenv("FLASK_DEBUG") == "1"
TITLE = "Anunbis"
SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", True)
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
JSON_AS_ASCII = False
JWT_ACCESS_TOKEN_EXPIRES = os.getenv(
    "FLASK_JWT_ACCESS_TOKEN_EXPIRES", timedelta(hours=1)
)

MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_USE_SSL = os.getenv("MAIL_USE_SSL") == "1"
MAIL_DEBUG = os.getenv("MAIL_DEBUG") == "1"
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "teste@gmail.com")
MAIL_DEFAULT_SENDER = MAIL_USERNAME
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "password")
MAIL_SUPPRESS_SEND = os.getenv("MAIL_SUPPRESS_SEND", "1") == "1"
