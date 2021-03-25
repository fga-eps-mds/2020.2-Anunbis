from ..dao import student_dao
from ...ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services
from ..entity.student import Student


def register_student(student):
    if course_services.get_course_id(student.id_course) is None:
        return {"message": "Course not found!"}, 404

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