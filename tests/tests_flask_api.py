from unittest import TestCase
from app.app import create_app
from app.model.dao import course_dao, discipline_dao
from flask import url_for
from json import loads

class TestFlaskBase(TestCase):
    def setUp(self):
        """ Start before all tests """
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"    # This create a in-memory sqlite db
        self.app.db.create_all()
        self.__create_base_entities()


    def tearDown(self):
        """ Start after all tests """
        self.app.db.drop_all()


    def create_student_token(self):
        login = self.client.post(url_for("restapi.login"), json=self.student)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['access_token']
        }


    def __create_base_entities(self):
        self.__create_base_course()
        self.__create_base_discipline()
        self.__create_base_professor()
        self.__create_base_student()

    def __create_base_course(self):
        self.course = {
            "id_course": "1",
            "name": "Engenharia de Software"
        }
        course_bd = course_dao.Course()
        course_bd.id_course = self.course['id_course']
        course_bd.name = self.course['name']
        self.app.db.session.add(course_bd)
        self.app.db.session.commit()

    def __create_base_discipline(self):
        self.discipline = {
            "discipline_code": "FGA01",
            "name": "Metodos Desenvolvimento de Software",
            "id_course": "1"
        }
        discipline_bd = discipline_dao.Discipline()
        discipline_bd.discipline_code = self.discipline['discipline_code']
        discipline_bd.name = self.discipline['name']
        discipline_bd.courses.append(course_dao.Course.query.filter_by(id_course = self.discipline['id_course']).first())
        self.app.db.session.add(discipline_bd)
        self.app.db.session.commit()
    
    def __create_base_professor(self):
        self.professor = {
            "name": "Carla Rocha",
            "reg_professor": "19002037777",
            "email": "19002037777@unb.br",
            "password": "123456789"
        }

        self.client.post(url_for("restapi.professorlist"), json=self.professor)

    def __create_base_student(self):
        self.student = {
            "name": "Primeiro Estudante",
            "reg_student": "190099999",
            "email": "190099999@aluno.unb.br",
            "password": "123456789",
            "id_course": "1"
        }

        self.client.post(url_for("restapi.studentlist"), json=self.student)

    