from flask_restful import Resource
from flask import request, make_response, jsonify, redirect, current_app
from ..schemas import user_schema
from ..services import auth_services, user_services


class LoginList(Resource):
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
            if not user_db.is_verified():
                auth_services.verify_email(user_db)
                return make_response(
                    jsonify({"message": "Email successfully sent!"}), 200
                )
            else:
                return make_response(
                    jsonify({"message": "User's e-mail already verified"}), 203
                )
        else:
            return make_response(jsonify({"message": "User not found!"}), 404)


def configure(api):
    api.add_resource(LoginList, "/login")
    api.add_resource(EmailVerifyList, "/auth/email")
