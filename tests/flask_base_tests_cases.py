from unittest import TestCase
from app.app import create_app
from app import config
from app.model import course, discipline, professor
from flask import url_for


class TestFlaskBase(TestCase):
    def setUp(self):  # This method run before each test
        self.app = create_app(config.TestConfig)
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()
        self.__create_atribute_entities()

    # This method run after each test
    def tearDown(self):
        self.app.db.drop_all()
        self.app_context.pop()

    def create_student_token(self):
        from tests_auth import valid_student_user

        student_user = valid_student_user(self)
        login = self.client.post(url_for("restapi.loginlist"), json=student_user)
        return {"Authorization": "Bearer " + login.json.get("access_token")}

    def create_professor_token(self):
        from tests_auth import valid_professor_user

        professor_user = valid_professor_user(self)
        login = self.client.post(url_for("restapi.loginlist"), json=professor_user)
        return {"Authorization": "Bearer " + login.json.get("access_token")}

    def create_base_entities(self):
        self.create_base_course()
        self.create_base_discipline()
        self.create_base_professor()
        self.create_base_student()

    def create_base_course(self):
        if self.course:
            return
        self.course = {"id_course": 1, "name": "Engenharia de Software"}
        course_bd = course.Course()
        course_bd.id_course = self.course["id_course"]
        course_bd.name = self.course["name"]
        self.app.db.session.add(course_bd)
        self.app.db.session.commit()

    def create_base_discipline(self):
        if self.discipline:
            return
        if self.course is None:
            self.create_base_course()

        self.discipline = {
            "discipline_code": "FGA01",
            "name": "Metodos Desenvolvimento de Software",
            "id_course": 1,
        }
        discipline_bd = discipline.Discipline()
        discipline_bd.discipline_code = self.discipline["discipline_code"]
        discipline_bd.name = self.discipline["name"]
        discipline_bd.courses.append(
            course.Course.query.filter_by(
                id_course=self.discipline["id_course"]
            ).first()
        )
        self.app.db.session.add(discipline_bd)
        self.app.db.session.commit()

    def create_base_professor(self):
        if self.professor:
            return
        from tests_professor import valid_professor

        self.professor = valid_professor()

        self.client.post(url_for("restapi.professorlist"), json=self.professor)
        professor_bd = professor.Professor.query.filter_by(
            reg_professor=self.professor["reg_professor"]
        ).first()
        self.professor["id_professor"] = professor_bd.id_professor
        if self.discipline is None:
            self.create_base_discipline()

        professor_bd.disciplines.append(
            discipline.Discipline.query.filter_by(
                discipline_code=self.discipline["discipline_code"]
            ).first()
        )
        self.app.db.session.commit()

    def create_base_student(self):
        if self.student:
            return
        if self.course is None:
            self.create_base_course()

        from tests_student import valid_student

        self.student = valid_student(self)

        self.client.post(url_for("restapi.studentlist"), json=self.student)

    # def create_base_post(self):
    #     if self.poste:
    #         return
    #     from tests_post import valid_post, valid_post_id
    #     self.poste = valid_post_id(self)

    #     self.client.post(url_for('restapi.postlist'), json=self.poste)

    def __create_atribute_entities(self):
        self.course = None
        self.discipline = None
        self.student = None
        self.professor = None
        # self.poste = None
