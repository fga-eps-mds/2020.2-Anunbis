from flask_restful import Resource
from flask import request, make_response, jsonify
from ..view import login_schema
from ..model.services import login_services
from ..model.entity.student import Student


class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            password = request.json['password']
            message, status_code = login_services.auth_student(email, password)
            return make_response(jsonify(message), status_code)

