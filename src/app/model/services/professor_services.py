from ..dao import professor_dao
from ...ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services
from ..entity.professor import Professor


def get_professor_name_contains(name):
    professors = professor_dao.Professor.query.filter(professor_dao.Professor.name.contains(name)).all()
    return professors

def register_professor(professor):

    try:
        professor_bd = professor_dao.Professor(reg_professor=professor.reg_professor, name=professor.name, 
                                            email=professor.email, password= professor.password)
        professor_bd.generate_password()                                        
        db.session.add(professor_bd)
        db.session.commit()
        return {"message":"Professor successfully registered!"},  201
    except IntegrityError:
        return {"message": "Professor already registered"}, 409

    return{"message": "Invalid request"}, 400


def get_professor_reg(reg_professor):
    professor = professor_dao.Professor.query.filter_by(reg_professor=reg_professor).first()


def get_professor_id(id_professor):
    professor = professor_dao.Professor.query.filter_by(id_professor=id_professor).first()
    return professor

