from ..dao import professor_dao

from ...ext.database import db
from sqlalchemy.exc import IntegrityError
from . import course_services
from ..entity.professor import Professor
from sqlalchemy import func


def get_professor_name_contains(name):
    professors = professor_dao.Professor.query.filter(func.lower(professor_dao.Professor.name).contains(name.lower())).all()
    return professors


def register_professor(professor):
    professor_bd = get_professor_name(professor.name)

    if professor_bd is None:
        return __build_professor(professor)
    elif __is_professor_made_by_admin(professor_bd):
        return __modify_professor(professor_bd, professor)
    else:
        return {"message": "This professor is already registered"}, 409


def get_professor_name(name):
    professor_bd = professor_dao.Professor.query.filter_by(name=name).first()
    return professor_bd


def __modify_professor(professor_bd, professor):
    try:
        professor_bd.email = professor.email
        professor_bd.reg_professor = professor.reg_professor
        professor_bd.password = professor.password
        professor_bd.generate_password()
        db.session.commit()
        return {"message": "Professor registered sucessfully"}, 201
    except IntegrityError:
        return {"message": "Professor already registered"}, 409

    return {"message": "Invalid request"}, 400


def __build_professor(professor):
        professor_bd = professor_dao.Professor(name=professor.name, reg_professor=professor.reg_professor,
                                               email=professor.email, password=professor.password)

        professor_bd.generate_password()
        db.session.add(professor_bd)
        db.session.commit()
        return {"message": "Professor sucessfully registered!"}, 201


def get_professor_reg(reg_professor):
    professor = professor_dao.Professor.query.filter_by(reg_professor=reg_professor).first()
    return professor


def get_professor_id(id_professor):
    professor = professor_dao.Professor.query.filter_by(id_professor=id_professor).first()
    return professor


def __is_professor_made_by_admin(professor_bd):
    return professor_bd.email is None

