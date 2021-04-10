from tests_flask_api import TestFlaskBase
from flask import url_for, jsonify


class TestCourseList(TestFlaskBase):
    def test_api_must_return_courses(self):
        expected = [self.course]

        response = self.client.get(url_for('restapi.courselist'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)