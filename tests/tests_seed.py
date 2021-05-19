from flask_base_tests_cases import TestFlaskBase
from app.ext import seed
from app.model import course, discipline, professor


class TestSeed(TestFlaskBase):
    def verify_json_in_db(self, json_name, modelClass):
        json_list = seed.read_json(json_name)
        obj_db = modelClass.query.all()
        self.assertEqual(len(json_list), len(obj_db))

    def test_must_run_seed(self):
        runner = self.app.test_cli_runner()
        result = runner.invoke(seed.seed)
        self.assertIn("seeds successfully added", result.output)

    def test_must_not_seed_duplicated(self):
        runner = self.app.test_cli_runner()
        runner.invoke(seed.seed)
        result = runner.invoke(seed.seed)
        self.assertIn("Objs already in database! Cant seed!", result.output)

    def test_must_seed_courses(self):
        seed.seed_courses()
        self.verify_json_in_db("courses", course.Course)

    def test_must_seed_disciplines(self):
        seed.seed_disciplines()
        self.verify_json_in_db("disciplines", discipline.Discipline)

    def test_must_seed_professor(self):
        exit_code, disciplines_dict = seed.seed_disciplines()
        seed.seed_professor(disciplines_dict)
        self.assertEqual(exit_code, 0)
        self.verify_json_in_db("professor", professor.Professor)
