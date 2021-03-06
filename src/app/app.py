from flask import Flask
from app.ext import database
from app.blueprints import restapi, schemas
from . import config

def minimal_app():
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def create_app():
    app = minimal_app()
    database.init_app(app)
    schemas.init_app(app)
    restapi.init_app(app)
    return app