from flask_base_tests_cases import TestFlaskBase
from app.model import student, user


class TestUser(TestFlaskBase):
    def test_must_block_password_access(self):
        try:
            std = student.Student(password="123456789")
            std.password
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def test_must_block_no_implemmented_method(self):
        try:
            usr = user.User()
            usr.is_professor()
            self.assertTrue(False)
        except NotImplementedError:
            self.assertTrue(True)
