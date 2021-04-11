from flask_base_tests_cases import TestFlaskBase
from flask import url_for
from app.model.dao import professor_dao

class TestProfessorList(TestFlaskBase):

    def post(self, json):
        return self.client.post(url_for("restapi.professorlist"), json=json)

    def valid_professor(self):
        return {
            "name": "Carla Rocha",
            "reg_professor": "19002037777",
            "email": "19002037777@unb.br",
            "password": "123456789"
        }
        
    def create_professor_made_by_admin(self, name):
        professor_bd = professor_dao.Professor()
        professor_bd.name = name
        self.app.db.session.add(professor_bd)
        self.app.db.session.commit()

    def test_api_must_register_a_valid_professor(self):
        professor = self.valid_professor()
        status_code_expected = 201

        response = self.post(professor)
        self.assertEqual(response.status_code, status_code_expected)

    def test_api_must_validate_professor_already_registered(self):
        self.create_base_professor()
        professor = self.professor
        response = self.post(professor)

        expected_json = {"message":"This professor is already registered"}
        expected_status_code = 409

        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json, expected_json)

    def test_api_must_register_professor_made_by_admin(self):
        professor = self.valid_professor()
        self.create_professor_made_by_admin(name=professor['name'])
        
        response = self.post(professor)
        self.assertEqual(response.status_code, 201)
        
    def test_api_must_validate_professor_made_by_admin_with_email_already_registered(self):
        self.create_base_professor()
        professor = self.valid_professor()
        professor['name'] = "Testing asduhdsauhsda"
        professor['email'] = self.professor['email']
        self.create_professor_made_by_admin(name=professor['name'])
        
        response = self.post(professor)
        self.assertEqual(response.status_code, 409)
    
    def test_api_must_validate_professor_made_by_admin_with_reg_already_registered(self):
        self.create_base_professor()
        professor = self.valid_professor()
        professor['name'] = "Testing asduhdsauhsda"
        professor['reg_professor'] = self.professor['reg_professor']
        self.create_professor_made_by_admin(name=professor['name'])
        
        response = self.post(professor)
        self.assertEqual(response.status_code, 409)

    def test_api_must_validate_empty_professor(self):
        professor = {}

        response = self.post(professor)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['email'])
        self.assertIsNotNone(response.json['reg_professor'])
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_attributes_types(self):
        professor = {
            "name": 1234,
            "reg_professor": "abc",
            "email": "abcunb.br",
            "password": "abc"
        }

        response = self.post(professor)

        expected = 400
        self.assertEqual(response.status_code, expected)
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['reg_professor'])
        self.assertIsNotNone(response.json['email'])
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_attributes_min_range(self):
        professor = self.valid_professor()
        professor['reg_professor'] = -1
        professor['name'] = "a"
        professor['password'] = "123"

        response = self.post(professor)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['reg_professor'])
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_attributes_max_range(self):
        professor = self.valid_professor()
        professor['name'] = "a"*256
        professor['password'] = "1"*101

        response = self.post(professor)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['name'])
        self.assertIsNotNone(response.json['password'])

    def test_api_must_validate_email_format(self):
        email = "qualquer_coisa@email.com"
        professor = self.valid_professor()
        professor['email'] = email

        response = self.post(professor)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'][0], "The email must be name(matricula)@unb.br")

    def test_api_must_validate_email_len(self):
        email = '1'*100 + "@unb.br"
        professor = self.valid_professor()
        professor['email'] = email

        response = self.post(professor)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['email'])


class TestProfessorDetail(TestFlaskBase):
    def get(self, name, headers):
        return self.client.get(url_for('restapi.professordetail', name=name), headers=headers)
    
    def test_api_must_return_professors_by_name_substring(self):
        headers = self.create_student_token()
        self.create_base_professor()
        name_substring = self.professor['name'][1].upper()
        
        response = self.get(name_substring, headers)

        json_attributes = list(response.json[0].keys())
        expected_json_attributes = ['disciplines', 'id_professor', 'name', 'posts', 'rating']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_attributes, expected_json_attributes)
        self.assertEqual(response.json[0]['name'], self.professor['name'])
        self.assertEqual(response.json[0]['posts'], [])

    def test_api_must_require_token(self):
        self.create_base_professor()
        name_substring = self.professor['name'][1].upper()
        
        response = self.get(name_substring, None)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'msg': 'Missing Authorization Header'})

    def test_api_must_not_return_private_attributes(self):
        headers = self.create_student_token()
        self.create_base_professor()
        name_substring = self.professor['name'][1].upper()
        
        response = self.get(name_substring, headers)

        json_attributes = list(response.json[0].keys())
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('email', json_attributes)
        self.assertNotIn('password', json_attributes)
        self.assertNotIn('reg_student', json_attributes)
