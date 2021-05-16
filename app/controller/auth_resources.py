from flask_restful import Resource
from flask import request, make_response, jsonify, redirect, current_app
from ..schemas import user_schema
from ..services import auth_services
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, current_user


class LoginList(Resource):
    def post(self):
        try:
            ls = user_schema.UserSchema()
            user = ls.load(request.json)
            user, status_code = auth_services.auth_user(user)
            return make_response(jsonify(user), status_code)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


class EmailVerifyList(Resource):
    def get(self):
        token_sended = request.args.get("token")
        message = auth_services.active_email_user(token_sended)
        if message:
            message["contact_us"] = current_app.config["ANUNBIS_FRONTEND_URI"]
            return make_response(jsonify(message), 400)
        else:
            return redirect(current_app.config["ANUNBIS_FRONTEND_URI"])


class TestEmail(Resource):
    @jwt_required()
    def get(self):
        user = current_user
        auth_services.verify_email(user)
        return make_response("Recebido", 200)


def configure(api):
    api.add_resource(LoginList, "/login")
    api.add_resource(EmailVerifyList, "/auth/email")
    api.add_resource(TestEmail, "/tests")
