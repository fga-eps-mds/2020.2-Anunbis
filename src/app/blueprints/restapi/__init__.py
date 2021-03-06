from flask import Blueprint, redirect, url_for
from flask_restful import Api

url_prefix="/anunbis/api/"
bp = Blueprint("restapi", __name__, url_prefix=url_prefix)
api = Api(bp)


def init_app(app):
    from . import home_resources
    api.add_resource(home_resources.HomeResource, "/")
    app.register_blueprint(bp)

    @app.route("/")
    def redirect_home():
        return redirect(url_prefix)