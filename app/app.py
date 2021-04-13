from flask import Flask
from .ext import database
from . import controller, view, model
from . import config


def minimal_app():
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def create_app():
    app = minimal_app()
    database.init_app(app)
    controller.init_app(app)
    view.init_app(app)
    model.init_app(app)
    return app