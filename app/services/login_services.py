from . import student_services
from . import professor_services
from flask_jwt_extended import create_access_token
from datetime import timedelta
from ..schemas.student_schema import StudentSchema
from ..schemas.professor_schema import ProfessorSchema

def auth_user(user):
    if user.is_professor():
        return  auth_professor(user)
    else:
        return auth_student(user)

def auth_student(user):
    student_db = student_services.get_student_email(user.email)
    ss = StudentSchema(only=['reg_student', 'name', 'email', 'id_course'])

    if student_db and student_db.verify_password(user.password):
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

def auth_professor(user):
    professor_db = professor_services.get_professor_email(user.email)
    ps = ProfessorSchema(only=['reg_professor','name','email'])

    if professor_db and professor_db.verify_password(user.password):
        access_token = create_access_token(
            identity = professor_db.reg_professor,
            expires_delta=timedelta(minutes=20)
        )
        return {
            'access_token': access_token,
            'message':'login accepted',
            'professor': ps.dump(professor_db)
        }, 200
    else:
        return {
            'message': 'Password or Email invalid'
        }, 401


