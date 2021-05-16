from flask_jwt_extended import create_access_token, decode_token
from flask import current_app
from ..schemas.student_schema import StudentSchema
from ..schemas.professor_schema import ProfessorSchema
from datetime import timedelta
from ..ext.email import send_verify_email
from . import user_services


def auth_user(user_json):
    user_db = user_services.get(email=user_json.get("email"))
    if user_db and user_db.verify_password(user_json.get("password")):
        if user_db.is_verified() or current_app.testing:
            return create_login(user_db)
        else:
            return {
                "message": "User's email not actived. Please, active your e-mail!"
            }, 203
    return {"message": "Email or Password invalid"}, 401


def create_login(user_db):
    access_token = create_access_token(
        identity=user_db,
        additional_claims={"is_student": not user_db.is_professor()},
    )
    schema = (
        ProfessorSchema(only=["reg_professor", "name", "email"])
        if user_db.is_professor()
        else StudentSchema(only=["reg_student", "name", "email", "id_course"])
    )
    return {
        "access_token": access_token,
        "message": "login accepted",
        "user": schema.dump(user_db),
    }, 200


def verify_email(user_db):
    token = create_access_token(identity=user_db, expires_delta=timedelta(hours=1))
    send_verify_email(user_db, token)


def active_email_user(token_send):
    try:
        token_verified = decode_token(token_send)
        reg_user = token_verified.get("sub")
        user_db = user_services.get(reg=reg_user)
        user_db.active_user()
        user_db.save_changes()
    except Exception:
        return {"message": "Token invalid"}
