from flask_jwt_extended import create_access_token
from ..schemas.student_schema import StudentSchema
from ..schemas.professor_schema import ProfessorSchema
from ..model.user import User


def auth_user(user):
    user = User(email=user.get("email"), password=user.get("password"))
    user_db = user.get()
    if user_db and user_db.verify_password(user.password):
        access_token = create_access_token(
            identity=user_db, additional_claims={"is_student": not user.is_professor()}
        )
        schema = (
            ProfessorSchema(only=["reg_professor", "name", "email"])
            if user.is_professor()
            else StudentSchema(only=["reg_student", "name", "email", "id_course"])
        )
        return {
            "access_token": access_token,
            "message": "login accepted",
            "user": schema.dump(user_db),
        }, 200

    return {"message": "Email or Password invalid"}, 401
