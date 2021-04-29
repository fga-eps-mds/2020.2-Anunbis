from flask_base_tests_cases import TestFlaskBase
from flask import url_for, jsonify
from .tests_post import register_post

def valid_student_report(self):
    self.create_base_entities()
    self.create_base_post()
    return{
        "id_post": self.post['id_post'],
        "reg_student": self.student['reg_student'],
        "id_professor": None,
        "content": "Comentario me ofendeu",
        "offensive": True,
        "prejudice": False,
        "unrelated": False,
        "others": False
    }

def valid_professor_report(self):
    self.create_base_entities()
    self.register_post()
    return{
        "id_post": self.post['id_post'],
        "reg_student": None,
        "id_professor": self.professor['id_professor'],
        "content": "Comentario me ofendeu",
        "offensive": True,
        "prejudice": False,
        "unrelated": False,
        "others": False
    }

def valid_id_report(self):
    return {
        "id_report": 1,
    } 

def register_student_report(self, report=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if report is None:
        report = valid_student_report(self)

    return self.client.post(url_for('restapi.reportlist'), json=report, headers=headers)

def register_professor_report(self, report=None, headers=None):
    if headers is None:
        headers = self.create_professor_token()
    if report is None:
        report = valid_professor_report(self)

    return self.client.post(url_for('restapi.reportlist'), json=report, headers=headers)

class TestReportList(TestFlaskBase):

    def test_api_must_register_a_valid_student_report(self):
        report = valid_student_report(self)
        response = register_student_report(self, report=report)
        self.assertEqual(response.status_code, 201)

    def test_api_must_register_a_valid_professor_report(self):
        report = valid_professor_report(self)
        response = register_professor_report(self, report=report)
        self.assertEqual(response.status_code, 201)

    def test_api_must_validate_no_token_student(self):
        report = valid_student_report(self)
        response = register_student_report(self, report=report, headers={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['msg'], 'Missing Authorization Header')

    def test_api_must_validate_no_token_professor(self):
        report = valid_professor_report(self)
        response = register_professor_report(self, report=report, headers={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['msg'], 'Missing Authorization Header')

    def test_api_must_validate_empty_attributes_student(self):
        report = {}
        response = register_student_report(self, report=report)

        expected_json_keys = ['id_post', 'content', 'offensive', 'prejudice', 'unrelated', 'others']
        json_keys = list(response.json.keys())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_keys, expected_json_keys)

    def test_api_must_validate_empty_attributes_professor(self):
        report = {}
        response = register_professor_report(self, report=report)

        expected_json_keys = ['id_post', 'content', 'offensive', 'prejudice', 'unrelated', 'others']
        json_keys = list(response.json.keys())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_keys, expected_json_keys)

    def test_api_must_validate_attributes_min_student(self):
        report = valid_student_report(self)
        report['content'] = ""
        response = register_student_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])

    def test_api_must_validate_attributes_min_student(self):
        report = valid_student_report(self)
        report['content'] = ""
        response = register_student_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])

    def test_api_must_validate_attributes_min_professor(self):
        report = valid_professor_report(self)
        report['content'] = ""
        response = register_professor_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])

    def test_api_must_validate_attributes_max_student(self):
        report = valid_student_report(self)
        report['content'] = "a"*121
        response = register_student_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])

    def test_api_must_validate_attributes_max_professor(self):
        report = valid_professor_report(self)
        report['content'] = "a"*121
        response = register_professor_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])

    def test_api_must_validate_student_different_from_tokens(self):
        report = valid_student_report(self)
        report['reg_student'] = int(self.student['reg_student']) + 1
        response = register_student_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get('reg_student'))

    def test_api_must_validate_professor_different_from_tokens(self):
        report = valid_professor_report(self)
        report['id_professor'] = int(self.student['id_professor']) + 1
        response = register_professor_report(self, report=report)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get('id_professor'))

    def test_api_must_validate_post_relationship_not_found_student(self):
        report = valid_student_report(self)
        report['id_post'] = self.post['id_post'] + 1
        response = register_student_report(self, report=report)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Post not found!")

    def test_api_must_validate_post_relationship_not_found_professor(self):
        report = valid_professor_report(self)
        report['id_post'] = self.post['id_post'] + 1
        response = register_professor_report(self, report=report)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Post not found!")


