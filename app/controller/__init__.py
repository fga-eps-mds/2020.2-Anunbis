from flask import Blueprint, redirect, url_for
from flask_restful import Api
from ..ext import auth, cors


def init_app(app):
    url_prefix = "/anunbis/api/"
    api_bp = Blueprint("restapi", __name__, url_prefix=url_prefix)
    api = Api(api_bp)

    auth.init_app(app)
    cors.init_app(app)

    from . import home_resources
    home_resources.configure(api)

    from . import course_resources
    course_resources.configure(api)

    from . import login_resources
    login_resources.configure(api)

    from . import post_resources
    post_resources.configure(api)

    from . import professor_resources
    professor_resources.configure(api)

    from . import student_resources
    student_resources.configure(api)

    app.register_blueprint(api_bp)

    @app.route("/")
    def redirect_home():
        return redirect(url_for("restapi.homelist"))
