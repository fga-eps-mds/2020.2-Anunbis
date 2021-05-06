from flask_base_tests_cases import TestFlaskBase
from flask import url_for


class TestHomeList(TestFlaskBase):
    def test_api_must_return_homepage(self):
        response = self.client.get(url_for("restapi.homelist"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Hello World of my heart!")

    def test_api_must_redirect_to_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
