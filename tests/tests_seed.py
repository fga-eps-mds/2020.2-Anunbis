from flask_base_tests_cases import TestFlaskBase
from app.ext import seed
from app.model import course, discipline, professor


class TestSeed(TestFlaskBase):
    def verify_json_in_db(self, json_name, modelClass):
        json_list = seed.read_json(json_name)
        obj_db = modelClass.query.all()
        self.assertEqual(len(json_list), len(obj_db))

    def test_must_seed(self):
        result = seed.seed()
        self.assertEqual(result, 0)

    def test_must_not_seed_duplicated(self):
        seed.seed()
        result = seed.seed()
        self.assertEqual(result, 1)

    def test_must_seed_courses(self):
        seed.seed_courses()
        self.verify_json_in_db("courses", course.Course)

    def test_must_seed_disciplines(self):
        seed.seed_disciplines()
        self.verify_json_in_db("disciplines", discipline.Discipline)

    def test_must_seed_course_discipline(self):
        seed.seed_course_discipline()
        self.verify_json_in_db("course_discipline", course.CourseDiscipline)

    def test_must_seed_professor(self):
        seed.seed_professor()
        self.verify_json_in_db("professor", professor.Professor)

    def test_must_seed_professor_discipline(self):
        seed.seed_professor_discipline()
        self.verify_json_in_db("professor_discipline", discipline.ProfessorDiscipline)
