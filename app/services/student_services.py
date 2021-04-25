from ..model.student import Student
from ..ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services


def register_student(student):
    validate, status_code = __validate_student_relationship(student)
    if validate:
        return validate, status_code

    try:
        student_bd = Student(reg_student=student.get('reg_student'), name=student.get('name'),
                             id_course=student.get('id_course'),
                             email=student.get('email'), password=student.get('password'))
        db.session.add(student_bd)
        db.session.commit()
        return {"message": "Student successfully registered!"}, 201
    except IntegrityError:
        return {"message": "Student already registered"}, 409


def __validate_student_relationship(student):
    if course_services.get_course_id(student.get('id_course')) is None:
        return {"message": "Course not found!"}, 404

    return None, 200


def get_student_reg(reg_student):
    student = Student.query.filter_by(reg_student=reg_student).first()
    return student


def delete_student_by_reg(reg_student):
    student_bd = Student.get(reg_student=reg_student)
    if student_bd:
        Student.delete(student_bd)
        return {'message': "Student successfully deleted!"}, 204


def modify_student(student):
    student_bd = Student.get(reg_student=student.get('reg_student'))
    if student_bd:
        student_bd.password = student.get('password')
        return {'message': 'Student successfully changed!'}, 200
