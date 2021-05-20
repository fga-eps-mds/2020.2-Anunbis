from flask_base_tests_cases import TestFlaskBase
from flask import url_for
from tests_post import register_post, valid_post_id


def valid_report(self):
    self.create_base_entities()
    register_post(self)
    return {
        "id_post": valid_post_id(self)["id_post"],
        "content": "Comentario me ofendeu",
        "offensive": True,
        "prejudice": False,
        "unrelated": False,
        "others": False,
    }


def register_report(self, report=None, headers=None):
    if headers is None:
        headers = self.create_student_token()
    if report is None:
        report = valid_report(self)

    return self.client.post(url_for("restapi.reportlist"), json=report, headers=headers)


class TestReportList(TestFlaskBase):
    def test_api_must_register_a_valid_report(self):
        report = valid_report(self)
        response = register_report(self, report=report)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("message"), "Report successfully added")

    def test_api_must_register_report_by_professor(self):
        report = valid_report(self)
        token = self.create_professor_token()
        response = register_report(self, report=report, headers=token)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("message"), "Report successfully added")

    def test_api_must_validate_no_token(self):
        report = valid_report(self)
        response = register_report(self, report=report, headers={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json.get("msg"), "Missing Authorization Header")

    def test_api_must_validate_empty_attributes(self):
        report = {}
        response = register_report(self, report=report)

        expected_json_keys = [
            "content",
            "id_post",
            "offensive",
            "others",
            "prejudice",
            "unrelated",
        ]
        json_keys = list(response.json.keys())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_keys, expected_json_keys)

    def test_api_must_validate_attributes_min(self):
        report = valid_report(self)
        report["content"] = ""
        response = register_report(self, report=report)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get("content"))

    def test_api_must_validate_attributes_max(self):
        report = valid_report(self)
        report["content"] = "a" * 121
        response = register_report(self, report=report)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get("content"))

    def test_api_must_validate_post_relationship_not_found(self):
        report = valid_report(self)
        report["id_post"] += 1
        response = register_report(self, report=report)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json.get("message"), "Post not found!")
