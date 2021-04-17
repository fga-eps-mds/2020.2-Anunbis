from ..dao import student_dao
from ...ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services
from ..entity.student import Student


def register_student(student):
    validate, status_code = __validate_student_relationship(student)
    if validate:
        return validate, status_code

    try:
        student_bd = student_dao.Student(reg_student=student.reg_student, name=student.name,
                                         id_course=student.id_course,
                                         email=student.email, password=student.password)
        student_bd.generate_password()
        db.session.add(student_bd)
        db.session.commit()
        return {"message": "Student successfully registered!"}, 201
    except IntegrityError:
        return {"message": "Student already registered"}, 409

    return {"message": "Invalid request"}, 400



def get_student_email(email):
    student = student_dao.Student.query.filter_by(email=email).first()
    return student

def __validate_student_relationship(student):
    if course_services.get_course_id(student.id_course) is None:
        return {"message": "Course not found!"}, 404

    return None, 200

def get_student_reg(reg_student):
    student = student_dao.Student.query.filter_by(reg_student=reg_student).first()
    return student

def delete_student_by_reg(reg_student):
    student_bd = student_dao.Student.get(reg_student=reg_student)
    if student_bd:
        student_dao.Student.delete(student_bd)
        return {'message': "Student successfully deleted!"}, 204
    else:
        return {'message': "Student not found!"}, 404

def modify_student(student):
    student_bd = student_dao.Student.get(reg_student=student.reg_student)
    if student_bd:
        student_bd.modify_student(student)
        return {'message': 'Student successfully changed!' }, 200

    
