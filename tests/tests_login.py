from flask_base_tests_cases import TestFlaskBase
from flask import url_for


class TestLogin(TestFlaskBase):
    
    def post(self, user):
        return self.client.post(url_for('restapi.loginlist'), json=user)

    def valid_student_user(self):
        self.create_base_student()
        return {
            'email': self.student['email'],
            'password': self.student['password']
        }
    
    def test_must_retun_token_from_a_valid_student(self):
        user = self.valid_student_user()

        response = self.post(user)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['access_token'])
        self.assertTrue(len(response.json['access_token']) > 0)

    def test_must_return_student_information(self):
        user = self.valid_student_user()

        response = self.post(user)

        student_expected = {
            'reg_student': self.student['reg_student'],
            'name': self.student['name'],
            'email': self.student['email'],
            'id_course': self.student['id_course']
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['student'], student_expected)

    def test_api_must_validate_student_not_registered(self):
        from tests_student import valid_student
        student = valid_student(self)
        user = {
            'email': student['email'],
            'password': student['password']
        }

        response = self.post(user)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Email or Password invalid' )
    
    def test_api_must_validate_student_wrong_password(self):
        user = self.valid_student_user()
        user['password'] = user['password'] + "assadd"

        response = self.post(user)
        self.assertEqual(response.json['message'], 'Email or Password invalid')

    def test_api_must_validate_empty_attributes(self):
        user = {}

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['email'])
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_password_min_len(self):
        user = self.valid_student_user()
        user['password'] = "1234567"

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_password_max_len(self):
        user = self.valid_student_user()
        user['password'] = "1"*101

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_email_max_len(self):
        user = self.valid_student_user()
        user['email'] = "1"*101 + "@aluno.unb.br"

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['email'])

    def test_api_must_validate_email_format(self):
        user = self.valid_student_user()
        user['email'] = "123456789@gmail.com"

        response = self.post(user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'][0], "The email must be matricula@aluno.unb.br")