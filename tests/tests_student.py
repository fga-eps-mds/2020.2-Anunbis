from flask_base_tests_cases import TestFlaskBase
from flask import url_for


class TestStudentList(TestFlaskBase):

    def post(self, json):
        return self.client.post(url_for("restapi.studentlist"), json=json)

    def test_api_must_register(self):
        self.create_base_course()
        student = {
            "name": "Testing Student",
            "reg_student": "190020000",
            "id_course": "1",
            "email": "190020000@aluno.unb.br",
            "password": "password"
        }
        response = self.post(student)
        self.assertEqual(response.status_code, 201)

    def test_must_validate_with_no_attributes(self):
        student = {}
        expected = ['email', 'id_course', 'name', 'password', 'reg_student']
        response = self.post(student)

        self.assertEqual(list(response.json.keys()), expected)

    def test_must_validate_string_attributes(self):
        student = {
            "name": "",
            "reg_student": "190020000",
            "id_course": "1",
            "email": 123,
            "password": 123456789
        }
        response = self.post(student)
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['email'])
        self.assertIsNotNone(response.json['password'])

    def test_must_validate_integer_attributes(self):
        student = {
            "name": "Testing Student",
            "reg_student": "19002asdasadssd0000",
            "id_course": "asddsaadadad1",
            "email": "190020000@aluno.unb.br",
            "password": "password"
        }
        response = self.post(student)
        self.assertIsNotNone(response.json['id_course'])
        self.assertIsNotNone(response.json['reg_student'])


