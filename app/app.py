from flask import Flask
from .ext import database, migrate, seed, swagger, auth, cors, email
from . import controller, schemas
from . import config


def minimal_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SWAGGER'] = {
        "swagger": "2.0",
        "info": {
            "title": "Anunbis back-end",
            "description": "Here is the Anunbis backend documentation API, where you can find about all of our methods and how they work. ",
            "contact": {
                "email": "anunbis.team@gmail.com",
                "url": "http://localhost:3000/",
            },
            "termsOfService": "http://localhost:3000/#contact",
            "version": "0.0.1"
        },
    }
    return app


def create_app(config_class=None):
    app = minimal_app(
        config.DevConfig if config_class is None else config_class)
    database.init_app(app)
    migrate.init_app(app)
    controller.init_app(app)
    auth.init_app(app)
    cors.init_app(app)
    schemas.init_app(app)
    seed.init_app(app)
    email.init_app(app)
    swagger.init_app(app)
    return app
