from ..model.student import Student
from ..ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services


def register_student(student):
    validate, status_code = __validate_student_relationship(student)
    if validate:
        return validate, status_code

    try:
        student_bd = Student(
            reg_student=student.get("reg_student"),
            name=student.get("name"),
            id_course=student.get("id_course"),
            email=student.get("email"),
            password=student.get("password"),
        )
        db.session.add(student_bd)
        db.session.commit()
        return {"message": "Student successfully registered!"}, 201
    except IntegrityError:
        return {"message": "Student already registered"}, 409


def __validate_student_relationship(student):
    if course_services.get_course_id(student.get("id_course")) is None:
        return {"message": "Course not found!"}, 404

    return None, 200


def delete_student(student_db):
    Student.delete(student_db)
    return {"message": "Student successfully deleted!"}, 204


def modify_student(student_db, student_new):
    student_db.password = student_new.get("password")
    db.session.commit()
    return {"message": "Student successfully changed!"}, 200
