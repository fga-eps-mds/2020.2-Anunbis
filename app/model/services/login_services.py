from . import student_services
from flask_jwt_extended import create_access_token
from datetime import timedelta
from ...view.student_schema import StudentSchema


def auth_student(email, password):
    student_db = student_services.get_student_email(email)
    ss = StudentSchema(only=['reg_student', 'name', 'email', 'id_course'])

    if student_db and student_db.verify_password(password):
        access_token = create_access_token(
            identity=student_db.reg_student,
            expires_delta=timedelta(minutes=20)
        )
        return {
            'access_token': access_token,
            'message': 'login accepted',
            'student': ss.dump(student_db)
        }, 200
    else:
        return {
            'message': 'Email or Password invalid'
        }, 401

