import json
from .database import db
from ..model import course
from ..model.discipline import Discipline
from ..model.professor import Professor
from sqlalchemy.exc import IntegrityError, InvalidRequestError
import click
from flask.cli import with_appcontext
from flask import current_app
import time


def current_milli_time():
    return round(time.time() * 1000)


def init_app(app):
    app.cli.add_command(seed)


@click.command()
@with_appcontext
def seed():
    initial_time = current_milli_time()
    exit_code = 0
    exit_code += seed_courses()
    exit_code_disciplines, disciplines_dict = seed_disciplines()
    exit_code += exit_code_disciplines
    exit_code += seed_professor(disciplines_dict)
    final_time = current_milli_time()
    print(f"time = {final_time - initial_time}ms")
    return 1 if exit_code > 0 else 0


def seed_courses():
    print("\nSeeding database with courses...")
    courses = read_json("courses")
    return add_seeds(courses, lambda c: course.Course(**c))


def seed_disciplines():
    disciplines_dict = {}

    def create_discipline(**d):
        discipline = Discipline(**d)
        disciplines_dict[d.get("discipline_code")] = discipline
        return discipline

    print("\nSeeding database with disciplines...")
    disciplines = read_json("disciplines")
    return add_seeds(disciplines, lambda d: create_discipline(**d)), disciplines_dict


def seed_professor(disciplines_dict):
    def create_professor(professor_json):
        professor = Professor(name=professor_json.get("name"))

        for discipline_json in professor_json.get("disciplines"):
            discipline = disciplines_dict.get(discipline_json.get("discipline_code"))
            if discipline:
                professor.disciplines.append(discipline)
        return professor

    print("\nSeeding database with professor...")
    professors = read_json("professor")
    return add_seeds(professors, create_professor)


def add_seeds(obj_list, modelFactory):
    try:
        for obj in obj_list:
            db.session.add(modelFactory(obj))
        db.session.commit()
        print(f"{len(obj_list)} seeds successfully added!\n")
        return 0
    except (IntegrityError, InvalidRequestError):
        print("Objs already in database! Cant seed!\n")
        return 1


def read_json(name):
    with current_app.open_resource(f"static/seeds/{name}.json") as fp:
        data = json.loads(fp.read())
    return data
