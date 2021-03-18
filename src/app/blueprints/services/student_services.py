from app.models import student_model
from app.ext.database import db
from sqlalchemy.exc import IntegrityError
from app.blueprints.services import course_services

def register_student(student):
    if course_services.get_course_id(student['id_course']) is None:
        return {"message": "Course not found!"}, 404

    try:
        student_bd = student_model.Student(reg_student=student['reg_student'], name=student['name'], id_course=student['id_course'],
                                           email=student['email'], password=student['password'])
        student_bd.generate_password()
        db.session.add(student_bd)
        db.session.commit()
        return {"message": "Student successfully registered!"}, 201
    except IntegrityError:
        return {"message": "Student already registered"}, 409

    return {"message": "Invalid request"}, 400

