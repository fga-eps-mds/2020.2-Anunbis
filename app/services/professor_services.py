from ..model.professor import Professor
from ..ext.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


def get_professor_name_contains(name):
    professors = Professor.query.filter(func.lower(
        Professor.name).contains(name.lower())).all()
    return professors


def get_professor_name(name):
    professor_bd = Professor.query.filter_by(name=name).first()
    return professor_bd


def get_professor_reg(reg_professor):
    professor = Professor.query.filter_by(reg_professor=reg_professor).first()
    return professor


def get_professor_id(id_professor):
    professor = Professor.query.filter_by(id_professor=id_professor).first()
    return professor


def register_professor(professor):
    professor_bd = get_professor_name(professor.get('name'))

    if professor_bd is None:
        return __build_professor(professor)
    elif __is_professor_made_by_admin(professor_bd):
        return __modify_professor(professor_bd, professor)
    else:
        return {"message": "This professor is already registered"}, 409


def __modify_professor(professor_bd, professor):
    try:
        professor_bd.email = professor.get('email')
        professor_bd.reg_professor = professor.get('reg_professor')
        professor_bd.password = professor.get('password')
        db.session.commit()
        return {"message": "Professor registered sucessfully"}, 201
    except IntegrityError:
        return {"message": "Professor already registered"}, 409

    return {"message": "Invalid request"}, 400


def __build_professor(professor):
    professor_bd = Professor(name=professor.get('name'), reg_professor=professor.get('reg_professor'),
                             email=professor.get('email'), password=professor.get('password'))

    db.session.add(professor_bd)
    db.session.commit()
    return {"message": "Professor sucessfully registered!"}, 201


def __is_professor_made_by_admin(professor_bd):
    return professor_bd.email is None


def validate_name(name):
    for char in name:
        if not char.isalpha():
            return {"message": "Name should have just letters!"}

    return None
