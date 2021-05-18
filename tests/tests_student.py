from flask_base_tests_cases import TestFlaskBase
from flask import url_for
from app.services import student_services, post_services
from tests_post import register_post, register_post_agree, register_post_disagree
from tests_report import register_report


def valid_student(self):
    self.create_base_course()
    return {
        "name": "Testing Student",
        "reg_student": 190020000,
        "id_course": 1,
        "email": "190020000@aluno.unb.br",
        "password": "password",
    }


class TestStudentPostList(TestFlaskBase):
    def post(self, json):
        return self.client.post(url_for("restapi.studentlist"), json=json)

    def test_api_must_register(self):
        student = valid_student(self)

        response = self.post(student)
        self.assertEqual(response.status_code, 201)

    def test_api_must_send_email_when_register(self):
        with self.app.mail.record_messages() as outbox:
            student = valid_student(self)

            response = self.post(student)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(len(outbox), 1)
            self.assertEqual(outbox[0].recipients, [student.get("email")])

    def test_must_validate_with_no_attributes(self):
        student = {}
        expected = ["email", "id_course", "name", "password", "reg_student"]
        response = self.post(student)

        self.assertEqual(list(response.json.keys()), expected)

    def test_must_validate_string_attributes(self):
        student = valid_student(self)
        student["name"] = ""
        student["email"] = 123
        student["password"] = 123456789

        response = self.post(student)
        self.assertIsNotNone(response.json["name"])
        self.assertIsNotNone(response.json["email"])
        self.assertIsNotNone(response.json["password"])

    def test_must_validate_integer_attributes(self):
        student = valid_student(self)
        student["id_course"] = "adsasadasdassd"
        student["reg_student"] = "asddasasddas"

        response = self.post(student)
        self.assertIsNotNone(response.json["id_course"])
        self.assertIsNotNone(response.json["reg_student"])

    def test_must_validate_course_not_found(self):
        student = valid_student(self)
        student["id_course"] = 10

        response = self.post(student)
        self.assertEqual(response.status_code, 404)
        self.assertIsNot(response.json["message"].lower().find("course"), -1)

    def test_must_not_register_duplicated(self):
        self.create_base_student()
        expected_status = 409

        response = self.post(self.student)

        self.assertEqual(response.status_code, expected_status)

    def test_must_validate_email_len_greater_than_100(self):
        email = "1" * 100 + "@aluno.unb.br"
        student = valid_student(self)
        student["email"] = email

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["email"][0], "The email must be lower than 100")

    def test_must_validate_email_format(self):
        email = "adsasdsa@gmail.com"
        student = valid_student(self)
        student["email"] = email

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json["email"][0], "The email must be matricula@aluno.unb.br"
        )

    def test_must_validate_negative_integer(self):
        student = valid_student(self)
        student["reg_student"] = -1
        student["id_course"] = -1

        response = self.post(student)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["reg_student"])
        self.assertIsNotNone(response.json["id_course"])


class TestStudentPutList(TestFlaskBase):
    def put(self, password, headers):
        return self.client.put(
            url_for("restapi.studentlist"), json=password, headers=headers
        )

    def test_api_must_modify_password(self):
        self.create_base_student()
        password = {"password": self.student["password"] + "123"}
        headers = self.create_student_token()

        response = self.put(password, headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            student_services.get(
                reg_student=self.student["reg_student"]
            ).verify_password(password.get("password"))
        )
        self.assertEqual(response.json["message"], "Student successfully changed!")

    def test_must_validate_password_length(self):
        self.create_base_student()
        password = {"password": "123"}
        headers = self.create_student_token()

        response = self.put(password, headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json["password"][0], "Length must be between 8 and 100."
        )

    def test_must_validate_null_password(self):
        self.create_base_student()
        password = {}
        headers = self.create_student_token()

        response = self.put(password, headers)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["password"])

    def test_api_validate_token(self):
        self.create_base_student()
        password = {"password": "123456789"}
        headers = None

        response = self.put(password, headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["msg"], "Missing Authorization Header")


class TestStudentDeleteList(TestFlaskBase):
    def delete(self, headers):
        return self.client.delete(url_for("restapi.studentlist"), headers=headers)

    def test_api_must_delete_student(self):
        self.create_base_student()
        headers = self.create_student_token()

        response = self.delete(headers)

        self.assertEqual(response.status_code, 204)
        self.assertIsNone(student_services.get(reg_student=self.student["reg_student"]))

    def test_api_must_validate_delete_on_deleted_student(self):
        self.create_base_student()
        headers = self.create_student_token()

        self.delete(headers)
        response = self.delete(headers)

        self.assertEqual(response.status_code, 401)

    def test_api_must_delete_student_posts(self):
        self.create_base_student()
        response_post = register_post(self)

        response = self.delete(self.create_student_token())

        self.assertEqual(response_post.status_code, 201)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(post_services.get(reg_student=self.student["reg_student"]))

    def test_api_must_delete_student_posts_agrees(self):
        self.create_base_student()
        register_post(self)
        register_post_agree(self)
        response = self.delete(self.create_student_token())

        self.assertEqual(response.status_code, 204)

    def test_api_must_delete_student_posts_disagrees(self):
        self.create_base_student()
        register_post(self)
        register_post_disagree(self)
        response = self.delete(self.create_student_token())

        self.assertEqual(response.status_code, 204)

    def test_api_must_delete_student_posts_reports(self):
        self.create_base_student()
        register_post(self)
        register_report(self)
        response = self.delete(self.create_student_token())

        self.assertEqual(response.status_code, 204)
