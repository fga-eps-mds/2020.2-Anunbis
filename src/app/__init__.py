from flask import Flask
from flask_restful import Api
from . import config
from .model import configure as configure_model
from .view import configure as configure_view
from .controller import configure as configure_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    
    configure_model(app)
    configure_view(app)
    configure_controller(app)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
