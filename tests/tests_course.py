from flask_base_tests_cases import TestFlaskBase
from flask import url_for


class TestCourseList(TestFlaskBase):
    def test_api_must_return_courses(self):
        self.create_base_course()
        expected = [self.course]

        response = self.client.get(url_for("restapi.courselist"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
