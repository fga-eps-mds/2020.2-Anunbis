from flask import Flask
from flask_restful import Api
from . import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    


    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app