import os
from datetime import timedelta


class BaseConfig:
    TITLE = "Anunbis"
    JSON_AS_ASCII = False
    MAIL_DEBUG = True
    ANUNBIS_FRONTEND_URI = os.getenv("ANUNBIS_FRONTEND_URI", "localhost:3000")
    ANUNBIS_BACKEND_URI = os.getenv("ANUNBIS_BACKEND_URI", "localhost:5000")


class DevConfig(BaseConfig):
    DEBUG = os.getenv("FLASK_DEBUG") == "1"
    SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", True)
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.getenv("TOKEN_EXPIRES_HOURS", 1)))
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 465))
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL") == "1"
    MAIL_DEBUG = os.getenv("MAIL_DEBUG") == "1"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "example@gmail.com")
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "password")
    MAIL_SUPPRESS_SEND = os.getenv("MAIL_SUPPRESS_SEND", "1") == "1"


class TestConfig(BaseConfig):
    TESTING = True
    JWT_SECRET_KEY = "anunbis-test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SUPPRESS_SEND = True
    MAIL_USERNAME = "test@gmail.com"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_PASSWORD = "password"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
