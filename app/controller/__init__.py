from marshmallow import ValidationError
from flask import Blueprint, redirect, url_for, make_response, jsonify
from flask_restful import Api


def init_app(app):
    url_prefix = "/anunbis/api/"
    api_bp = Blueprint("restapi", __name__, url_prefix=url_prefix)
    api = Api(api_bp)

    from . import course_resources

    course_resources.configure(api)

    from . import auth_resources

    auth_resources.configure(api)

    from . import post_resources

    post_resources.configure(api)

    from . import professor_resources

    professor_resources.configure(api)

    from . import student_resources

    student_resources.configure(api)

    from . import report_resources

    report_resources.configure(api)

    app.register_blueprint(api_bp)

    @app.route("/")
    def redirect_home():
        return redirect(url_for("flasgger.apidocs"))

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return make_response(jsonify(error.messages), 400)
