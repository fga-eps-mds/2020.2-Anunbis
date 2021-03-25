from flask import Blueprint, redirect, url_for
from flask_restful import Api
from ..ext import auth, cors

url_prefix="/anunbis/api/"
bp = Blueprint("restapi", __name__, url_prefix=url_prefix)
api = Api(bp)


def init_app(app):
    auth.init_app(app)
    cors.init_app(app)

    from . import home_resources, course_resources, student_resources, login_resources
    api.add_resource(home_resources.HomeResource, "/")
    api.add_resource(course_resources.CourseList, "/course")
    api.add_resource(student_resources.StudentList, "/student")
    api.add_resource(login_resources.LoginList, "/login")

    app.register_blueprint(bp)

    @app.route("/")
    def redirect_home():
        return redirect(url_prefix)
