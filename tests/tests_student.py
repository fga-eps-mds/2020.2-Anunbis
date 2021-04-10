from flask_base_tests_cases import TestFlaskBase
from flask import url_for

class TestStudentList(TestFlaskBase):
    def test_api_must_register_valid_student(self):
        self.create_base_course()
        student = {
            "name": "Testing Student",
            "reg_student": "190020000",
            "id_course": "1",
            "email": "190020000@aluno.unb.br",
            "password": "password"
        }
        response = self.client.post(url_for("restapi.studentlist"), json=student)
        self.assertEqual(response.status_code, 201)