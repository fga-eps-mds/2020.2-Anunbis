from flask_base_tests_cases import TestFlaskBase
from flask import url_for


def valid_post(self):
    self.create_base_entities()
    return {
        "id_professor": self.professor["id_professor"],
        "reg_student": self.student["reg_student"],
        "discipline_code": self.discipline["discipline_code"],
        "content": "Professor nota cinco",
        "didactic": "5",
        "metod": "5",
        "avaliations": "5",
        "disponibility": "5",
        "is_anonymous": True,
    }


def valid_post_id(self):
    return {
        "id_post": 1,
    }


def get_posts(self, headers=None):
    if headers is None:
        headers = self.create_student_token()

    return self.client.get(url_for("restapi.postlist"), headers=headers)


def register_post(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post(self)

    return self.client.post(url_for("restapi.postlist"), json=post, headers=headers)


def register_post_agree(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post_id(self)
    return self.client.post(
        url_for("restapi.postagreeslist"), json=post, headers=headers
    )


def register_post_disagree(self, post=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if post is None:
        post = valid_post_id(self)

    return self.client.post(
        url_for("restapi.postdisagreeslist"), json=post, headers=headers
    )


class TestPostList(TestFlaskBase):
    def test_api_must_register_a_valid_post(self):
        post = valid_post(self)
        response = register_post(self, post=post)
        self.assertEqual(response.status_code, 201)

    def test_api_must_validate_no_token(self):
        post = valid_post(self)
        response = register_post(self, post=post, headers={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["msg"], "Missing Authorization Header")

    def test_api_must_validate_empty_attributes(self):
        post = {}
        response = register_post(self, post=post)

        expected_json_keys = [
            "avaliations",
            "content",
            "didactic",
            "discipline_code",
            "disponibility",
            "id_professor",
            "is_anonymous",
            "metod",
            "reg_student",
        ]
        json_keys = list(response.json.keys())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_keys, expected_json_keys)

    def test_api_must_validate_attributes_min(self):
        post = valid_post(self)

        post["content"] = ""
        post["didactic"] = 0
        post["metod"] = 0
        post["avaliations"] = 0
        post["disponibility"] = 0

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["content"])
        self.assertIsNotNone(response.json["didactic"])
        self.assertIsNotNone(response.json["metod"])
        self.assertIsNotNone(response.json["avaliations"])
        self.assertIsNotNone(response.json["disponibility"])

    def test_api_must_validate_attributes_max(self):
        post = valid_post(self)
        post["content"] = "a" * 481
        post["didactic"] = 6
        post["metod"] = 6
        post["avaliations"] = 6
        post["disponibility"] = 6

        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["content"])
        self.assertIsNotNone(response.json["didactic"])
        self.assertIsNotNone(response.json["metod"])
        self.assertIsNotNone(response.json["avaliations"])
        self.assertIsNotNone(response.json["disponibility"])

    def test_api_must_validate_professor_relationship_not_found(self):
        post = valid_post(self)
        post["id_professor"] = "10"
        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Professor not found!")

    def test_api_must_validate_student_different_from_tokens(self):
        post = valid_post(self)
        post["reg_student"] = int(self.student["reg_student"]) + 1
        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get("reg_student"))

    def test_api_must_validate_discipline_relationship_not_found(self):
        post = valid_post(self)
        post["discipline_code"] = self.discipline["discipline_code"] + "asuhasusah"
        response = register_post(self, post=post)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Discipline not found!")


class TestGetPostList(TestFlaskBase):
    def test_must_get_student_post_found_empty(self):
        response = get_posts(self)
        status_code_expected = 200

        self.assertEqual(response.status_code, status_code_expected)
        self.assertEqual(response.json, [])

    def test_must_get_student_post_found(self):
        register_post(self)
        response = get_posts(self)
        status_code_expected = 200

        self.assertEqual(response.status_code, status_code_expected)
        self.assertEqual(response.json[0]["content"], valid_post(self)["content"])

    def test_must_get_posts_about_professor_found_empty(self):
        response = get_posts(self, self.create_professor_token())
        status_code_expected = 200

        self.assertEqual(response.status_code, status_code_expected)
        self.assertEqual(response.json, [])

    def test_must_get_posts_about_professor_found(self):
        register_post(self)
        response = get_posts(self, self.create_professor_token())
        status_code_expected = 200

        self.assertEqual(response.status_code, status_code_expected)
        self.assertEqual(response.json[0]["content"], valid_post(self)["content"])


class TestPostAgree(TestFlaskBase):
    def test_api_must_agree_post(self):
        register_post(self)
        response = register_post_agree(self)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 1, "disagrees": 0, "is_agreed": True, "is_disagreed": False},
        )

    def test_api_must_block_professor_token(self):
        register_post(self)
        response = register_post_agree(self, headers=self.create_professor_token())
        self.assertEqual(response.status_code, 403)

    def test_api_must_unagree_post(self):
        register_post(self)
        register_post_agree(self)
        response = register_post_agree(self)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 0, "disagrees": 0, "is_agreed": False, "is_disagreed": False},
        )

    def test_api_must_agree_after_disagree(self):
        post = valid_post(self)
        register_post(self, post=post)
        register_post_disagree(self)
        response = register_post_agree(self)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 1, "disagrees": 0, "is_agreed": True, "is_disagreed": False},
        )

    def test_api_must_validate_post_not_found_agree(self):
        register_post(self, 2)
        response = register_post_agree(self)
        self.assertEqual(response.status_code, 404)

    def test_api_must_not_validate_post_agree(self):
        post = {}
        register_post(self, post=post)
        response = register_post_agree(self, post)
        self.assertEqual(response.status_code, 400)

    def test_api_must_validate_token_agree(self):
        post = valid_post(self)
        register_post(self, post=post)
        response = register_post_agree(self, headers={})
        self.assertEqual(response.status_code, 401)


class TestPostDisagree(TestFlaskBase):
    def test_api_must_disagee_post(self):  # fail
        register_post(self)
        response = register_post_disagree(self)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 0, "disagrees": 1, "is_agreed": False, "is_disagreed": True},
        )

    def test_api_must_undisagree_post(self):  # fail
        register_post(self)
        register_post_disagree(self)
        response = register_post_disagree(self)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 0, "disagrees": 0, "is_agreed": False, "is_disagreed": False},
        )

    def test_api_must_disagree_after_agree(self):
        post = valid_post(self)
        register_post(self, post=post)
        register_post_agree(self)
        response = register_post_disagree(self)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["feedbacks"],
            {"agrees": 0, "disagrees": 1, "is_agreed": False, "is_disagreed": True},
        )

    def test_api_must_validate_post_not_found_disagree(self):
        register_post(self, 2)
        response = register_post_disagree(self)
        self.assertEqual(response.status_code, 404)

    def test_api_must_not_validate_post_disagree(self):
        post = {}
        register_post(self, post=post)
        response = register_post_disagree(self, post)
        self.assertEqual(response.status_code, 400)

    def test_api_must_validate_token_disagree(self):
        post = valid_post(self)
        register_post(self, post=post)
        response = register_post_disagree(self, headers={})
        self.assertEqual(response.status_code, 401)
