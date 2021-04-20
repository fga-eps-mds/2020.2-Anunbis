from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import login_schema
from ..services import login_services
from marshmallow import ValidationError


class LoginList(Resource):
    def post(self):
        try:
            ls = login_schema.LoginSchema()
            user = ls.load(request.json)
            message, status_code = login_services.auth_student(user)
            return make_response(jsonify(message), status_code)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


def configure(api):
    api.add_resource(LoginList, "/login")

