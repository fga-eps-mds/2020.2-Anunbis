from unittest import TestCase
from app.app import create_app
from app.model.dao import course_dao, discipline_dao, professor_dao
from flask import url_for
from json import loads


class TestFlaskBase(TestCase):
    def setUp(self):                                           # This method run before each test
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.config['JWT_SECRET_KEY'] = "anunbis-test"
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"  # This create a in-memory sqlite db
        self.app.db.create_all()
        self.__create_atribute_entities()

    def tearDown(self):                                         # This method run after each test
        self.app.db.drop_all()
        self.app_context.pop()

    def create_student_token(self):
        if self.student is None:
            self.create_base_student()

        json = {
            "email": self.student['email'],
            "password": self.student['password']
        }
        login = self.client.post(url_for("restapi.loginlist"), json=json)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['access_token']
        }

    def create_base_entities(self):
        self.create_base_course()
        self.create_base_discipline()
        self.create_base_professor()
        self.create_base_student()

    def create_base_course(self):
        self.course = {
            "id_course": 1,
            "name": "Engenharia de Software"
        }
        course_bd = course_dao.Course()
        course_bd.id_course = self.course['id_course']
        course_bd.name = self.course['name']
        self.app.db.session.add(course_bd)
        self.app.db.session.commit()

    def create_base_discipline(self):
        if self.course is None:
            self.create_base_course()

        self.discipline = {
            "discipline_code": "FGA01",
            "name": "Metodos Desenvolvimento de Software",
            "id_course": 1
        }
        discipline_bd = discipline_dao.Discipline()
        discipline_bd.discipline_code = self.discipline['discipline_code']
        discipline_bd.name = self.discipline['name']
        discipline_bd.courses.append(course_dao.Course.query.filter_by(id_course=self.discipline['id_course']).first())
        self.app.db.session.add(discipline_bd)
        self.app.db.session.commit()

    def create_base_professor(self):            
        self.professor = {
            "name": "Carla Rocha",
            "reg_professor": 19002037777,
            "email": "19002037777@unb.br",
            "password": "123456789"
        }

        self.client.post(url_for("restapi.professorlist"), json=self.professor)
        professor_bd = professor_dao.Professor.query.filter_by(reg_professor=self.professor['reg_professor']).first()
        self.professor['id_professor'] = professor_bd.id_professor
        if self.discipline is None:
            self.create_base_discipline()

        professor_bd.disciplines.append(discipline_dao.Discipline.query.filter_by(discipline_code=self.discipline['discipline_code']).first())
        self.app.db.session.commit()

    def create_base_student(self):
        if self.course is None:
            self.create_base_course()

        self.student = {
            "name": "Primeiro Estudante",
            "reg_student": 190099999,
            "email": "190099999@aluno.unb.br",
            "password": "123456789",
            "id_course": 1
        }

        self.client.post(url_for("restapi.studentlist"), json=self.student)

    def __create_atribute_entities(self):
        self.course = None
        self.discipline = None
        self.student = None
        self.professor = None
