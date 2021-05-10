from flask import Flask
from .ext import database, migrate, seed
from . import controller, schemas
from . import config


def minimal_app():
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def create_app():
    app = minimal_app()
    database.init_app(app)
    migrate.init_app(app)
    controller.init_app(app)
    schemas.init_app(app)
    cli_commands(app)
    return app


def cli_commands(app):
    @app.cli.command("seed")
    def seed_command():
        return seed.seed()
