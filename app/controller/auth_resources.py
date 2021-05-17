from flask_restful import Resource
from flask import request, make_response, jsonify, redirect, current_app
from ..schemas import user_schema
from ..services import auth_services, user_services
from ..docs.login import login_list_post
from flasgger import swag_from


class LoginList(Resource):
    @swag_from(login_list_post)
    def post(self):
        ls = user_schema.UserSchema()
        user = ls.load(request.json)
        user, status_code = auth_services.auth_user(user)
        return make_response(jsonify(user), status_code)


class EmailVerifyList(Resource):
    def get(self):
        token_sended = request.args.get("token")
        message = auth_services.active_email_user(token_sended)
        if message:
            message["contact_us"] = current_app.config["ANUNBIS_FRONTEND_URI"]
            return make_response(jsonify(message), 400)
        else:
            return redirect(current_app.config["ANUNBIS_FRONTEND_URI"])

    def post(self):
        email = user_schema.UserSchema(only=["email"]).load(request.json)
        user_db = user_services.get(**email)
        if user_db:
            message, status_code = auth_services.resend_verify_email(user_db)
            return make_response(jsonify(message), status_code)
        else:
            return make_response(jsonify({"message": "User not found!"}), 404)


def configure(api):
    api.add_resource(LoginList, "/login")
    api.add_resource(EmailVerifyList, "/auth/email")
