from flask import Blueprint, redirect, url_for
from flask_restful import Api
from ..ext import auth, cors

url_prefix="/anunbis/api/"
bp = Blueprint("restapi", __name__, url_prefix=url_prefix)
api = Api(bp)


def init_app(app):
    auth.init_app(app)
    cors.init_app(app)

    from . import home_resources, course_resources, student_resources, post_resources, professor_resources
    api.add_resource(home_resources.HomeResource, "/")
    api.add_resource(course_resources.CourseList, "/course")
    api.add_resource(student_resources.StudentList, "/student")
    api.add_resource(post_resources.PostList, "/post")
    api.add_resource(professor_resources.ProfessorDetail, "/professor/<string:name>")
    api.add_resource(professor_resources.ProfessorList, "/professor")

    app.register_blueprint(bp)

    @app.route("/")
    def redirect_home():
        return redirect(url_prefix)
