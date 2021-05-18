from flask_base_tests_cases import TestFlaskBase


class TestHomeList(TestFlaskBase):
    def test_api_must_redirect_to_docs(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
