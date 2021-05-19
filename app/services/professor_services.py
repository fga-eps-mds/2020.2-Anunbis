from ..model.professor import Professor
from ..ext.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from . import auth_services
import re


def get(**kwargs):
    return Professor.query.filter_by(**kwargs).first()


def get_by_email(email):
    return Professor.query.filter(
        func.lower(Professor.email) == email.lower()
    ).one_or_none()


def get_name_contains(name):
    professors = Professor.query.filter(
        func.lower(Professor.name).contains(name.lower())
    ).all()
    return professors


def register_professor(professor):
    name = re.sub("[ ]+", " ", professor.get("name").strip())
    professor_bd = get(name=name)

    if professor_bd is None:
        return __build_professor(professor)
    elif __is_professor_made_by_admin(professor_bd):
        return __modify_professor(professor_bd, professor)
    else:
        return {"message": "This professor is already registered"}, 409


def __modify_professor(professor_bd, professor):
    try:
        professor_bd.email = professor.get("email")
        professor_bd.reg_professor = professor.get("reg_professor")
        professor_bd.password = professor.get("password")
        db.session.commit()
        auth_services.verify_email(professor_bd)
        return {"message": "Professor registered sucessfully"}, 201
    except IntegrityError:
        return {"message": "Professor already registered"}, 409


def __build_professor(professor):
    try:
        professor_bd = Professor(
            name=professor.get("name"),
            reg_professor=professor.get("reg_professor"),
            email=professor.get("email"),
            password=professor.get("password"),
        )

        db.session.add(professor_bd)
        db.session.commit()
        auth_services.verify_email(professor_bd)
        return {"message": "Professor sucessfully registered!"}, 201
    except IntegrityError:
        return {"message": "Professor already registered"}, 409


def __is_professor_made_by_admin(professor_bd):
    return professor_bd.email is None


def modify_password_professor(professor_bd, professor_new):
    professor_bd.password = professor_new.get("password")
    db.session.commit()
    return {"message": "Professor password successfully changed!"}, 200


def delete_professor_login(professor_db):
    professor_db.clean_credentials()
    db.session.commit()
    return {"message": "Professor successfully deleted!"}, 204
