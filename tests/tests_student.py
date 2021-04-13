from flask_base_tests_cases import TestFlaskBase
from flask import url_for


class TestStudentList(TestFlaskBase):

    def post(self, json):
        return self.client.post(url_for("restapi.studentlist"), json=json)

    def test_api_must_register(self):
        student = valid_student(self)

        response = self.post(student)
        self.assertEqual(response.status_code, 201)

    def test_must_validate_with_no_attributes(self):
        student = {}
        expected = ['email', 'id_course', 'name', 'password', 'reg_student']
        response = self.post(student)

        self.assertEqual(list(response.json.keys()), expected)

    def test_must_validate_string_attributes(self):
        student = valid_student(self)
        student["name"] = ""
        student["email"] = 123
        student["password"] = 123456789 
 
        response = self.post(student)
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['email'])
        self.assertIsNotNone(response.json['password'])

    def test_must_validate_integer_attributes(self):
        student = valid_student(self)
        student['id_course'] = "adsasadasdassd"
        student['reg_student'] = "asddasasddas"

        response = self.post(student)
        self.assertIsNotNone(response.json['id_course'])
        self.assertIsNotNone(response.json['reg_student'])

    def test_must_validate_course_not_found(self):
        student = valid_student(self)
        student['id_course'] = 10

        response = self.post(student)
        self.assertEqual(response.status_code, 404)
        self.assertIsNot(response.json['message'].lower().find("course"), -1)

    def test_must_not_register_duplicated(self):
        self.create_base_student()
        expected_status = 409

        response = self.post(self.student)

        self.assertEqual(response.status_code, expected_status)

    def test_must_validate_email_len_greater_than_100(self):
        email = '1'*100 + "@aluno.unb.br"
        student = valid_student(self)
        student['email'] = email

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'][0], "The email must be lower than 100")

    def test_must_validate_email_format(self):
        email = "adsasdsa@gmail.com"
        expected = "The email must be matricula@aluno.unb.br"
        student = valid_student(self)
        student['email'] = email

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'][0], "The email must be matricula@aluno.unb.br")
    
    def test_must_validate_negative_integer(self):
        student = valid_student(self)
        student['reg_student'] = -1
        student['id_course'] = -1

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['reg_student'])
        self.assertIsNotNone(response.json['id_course'])

def valid_student(self):
    self.create_base_course()
    return {
        "name": "Testing Student",
        "reg_student": "190020000",
        "id_course": "1",
        "email": "190020000@aluno.unb.br",
        "password": "password"
    }