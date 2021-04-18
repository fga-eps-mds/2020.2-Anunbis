from flask_base_tests_cases import TestFlaskBase
from flask import url_for


def valid_post(self):
    self.create_base_entities()
    return {
        "id_post": 1,
        "id_professor": self.professor['id_professor'],
        "reg_student": self.student['reg_student'],
        "discipline_code": self.discipline['discipline_code'],
        "content": "Professor nota dez",
        "rating": "5",
        "is_anonymous": True
    } 

def register_post(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post(self)

    return self.client.post(url_for('restapi.postlist'), json=post, headers=headers)

def register_post_agree(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post(self)

    return self.client.post(url_for('restapi.postagreeslist'), json=post, headers=headers)

def register_post_disagree(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post(self)

    return self.client.post(url_for('restapi.postdisagreeslist'), json=post, headers=headers)


class TestPostList(TestFlaskBase):

    def test_api_must_register_a_valid_post(self):
        post = valid_post(self)

        response = register_post(self, post=post)
        self.assertEqual(response.status_code, 201)

    def test_api_must_validate_no_token(self):
        post = valid_post(self)

        response = register_post(self, post=post, headers={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['msg'], 'Missing Authorization Header')


    def test_api_must_validate_empty_attributes(self):
        post = {}

        response = register_post(self, post=post)

        expected_json_keys = ['content', 'discipline_code', 'id_post','id_professor', 'is_anonymous', 'rating', 'reg_student']
        json_keys = list(response.json.keys())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_keys, expected_json_keys)

    def test_api_must_validate_attributes_min(self):
        post = valid_post(self)
        post['content'] = ""
        post['rating'] = -1

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])
        self.assertIsNotNone(response.json['rating'])
    
    def test_api_must_validate_attributes_max(self):
        post = valid_post(self)
        post['content'] = "a"*481
        post['rating'] = 11

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json['content'])
        self.assertIsNotNone(response.json['rating'])

    def test_api_must_validate_professor_relationship_not_found(self):
        post = valid_post(self)
        post['id_professor'] = "10"

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Professor not found!")

    def test_api_must_validate_student_relationship_not_found(self):
        post = valid_post(self)
        post['reg_student'] = int(self.student['reg_student']) + 1

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Student not found!")

    def test_api_must_validate_discipline_relationship_not_found(self):
        post = valid_post(self)
        post['discipline_code'] = self.discipline['discipline_code'] + "asuhasusah"

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Discipline not found!")


class TestPostAgree(TestFlaskBase):
    def test_api_must_register_student_agree(self):
        post = valid_post(self)
        register_post(self, post=post)

        response = register_post_agree(self)
        self.assertEqual(response.status_code, 200)
        # verificar se o numero de curtida = 1

    def test_api_must_unagree_post(self):
        post = valid_post(self)
        register_post(self, post=post)

        register_post_agree(self)
        response = register_post_agree(self)
        self.assertEqual(response.status_code, 200)
        # verificar se o numero de curtida == 0

class TestPostDisagree(TestFlaskBase):

    def test_api_must_register_student_disagree(self):
        post = valid_post(self)
        register_post(self, post=post)
        response = register_postDisagree(self)
        self.assertEqual(response.status_code, 200)
        # verificar se o numero de agree = 1


    def test_api_must_undisagree_post(self):
        post = valid_post(self)
        register_post(self, post=post)
        register_post_disagree(self)
        response = register_postDisagree(self)
        self.assertEqual(response.status_code, 200)
        # verificar se o numero de disagree = 1
