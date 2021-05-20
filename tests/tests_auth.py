from flask_base_tests_cases import TestFlaskBase
from flask import url_for
from app.services import student_services, auth_services


def valid_professor_user(self):
    self.create_base_professor()
    return {"email": self.professor["email"], "password": self.professor["password"]}


def valid_student_user(self):
    self.create_base_student()
    return {"email": self.student["email"], "password": self.student["password"]}


class TestLogin(TestFlaskBase):
    def post(self, user):
        return self.client.post(url_for("restapi.loginlist"), json=user)

    def test_must_retun_token_from_a_valid_student(self):
        user = valid_student_user(self)

        response = self.post(user)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["access_token"])
        self.assertTrue(len(response.json["access_token"]) > 0)

    def test_must_return_student_information(self):
        user = valid_student_user(self)

        response = self.post(user)

        student_expected = {
            "reg_student": self.student["reg_student"],
            "name": self.student["name"],
            "email": self.student["email"],
            "id_course": self.student["id_course"],
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["user"], student_expected)

    def test_api_must_block_no_actived_user(self):
        self.app.config["MAIL_SUPPRESS_SEND"] = False
        user = valid_student_user(self)

        with self.app.mail.record_messages():
            response = self.post(user)
            self.assertEqual(response.status_code, 203)
            self.assertEqual(
                response.json.get("message"),
                "User's email not actived. Please, active your e-mail!",
            )

    def test_api_must_validate_student_not_registered(self):
        from tests_student import valid_student

        student = valid_student(self)
        user = {"email": student["email"], "password": student["password"]}

        response = self.post(user)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["message"], "Email or Password invalid")

    def test_api_must_validate_student_wrong_password(self):
        user = valid_student_user(self)
        user["password"] = user["password"] + "assadd"

        response = self.post(user)
        self.assertEqual(response.json["message"], "Email or Password invalid")

    def test_api_must_validate_empty_attributes(self):
        user = {}

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["email"])
        self.assertIsNotNone(response.json["password"])

    def test_api_must_validate_password_min_len(self):
        user = valid_student_user(self)
        user["password"] = "1234567"

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["password"])

    def test_api_must_validate_password_max_len(self):
        user = valid_student_user(self)
        user["password"] = "1" * 101

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["password"])

    def test_api_must_validate_email_max_len(self):
        user = valid_student_user(self)
        user["email"] = "1" * 101 + "@aluno.unb.br"

        response = self.post(user)

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["email"])

    def test_api_must_validate_email_format(self):
        user = valid_student_user(self)
        user["email"] = "123456789@gmail.com"

        response = self.post(user)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["email"][0])

    def test_api_must_validate_student_email_format(self):
        user = valid_student_user(self)
        user["email"] = "123456789@aluno.gmail.com"

        response = self.post(user)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json["email"][0])

    def test_login_valid_professor_user_user(self):
        professor = valid_professor_user(self)
        expected_status_code = 200

        response = self.post(professor)
        self.assertIsNotNone(response.json["access_token"])
        self.assertEqual(response.status_code, expected_status_code)
        self.assertIsNotNone(response.json)
        self.assertTrue(len(response.json["access_token"]) > 0)

    def test_login_not_registered(self):
        valid_professor_user(self)

        professor_diferente = {"email": "19002038888@unb.br", "password": "987654321"}
        expected_status_code = 401
        expected_json = {"message": "Email or Password invalid"}

        response = self.post(professor_diferente)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json, expected_json)

    def test_login_not_fulfilled(self):
        professor = {}
        expected_status_code = 400
        expected_json = {
            "email": ["Missing data for required field."],
            "password": ["Missing data for required field."],
        }

        response = self.post(professor)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json, expected_json)

    def test_max_email_and_password_login(self):
        professor = {
            "email": "0123456789" * 101 + "@unb.br",
            "password": "0123456789" * 101,
        }
        expected_status_code = 400
        expected_json = {
            "email": ["The email must be lower than 100"],
            "password": ["Length must be between 8 and 100."],
        }

        response = self.post(professor)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json, expected_json)

    def test_invalid_format_email_and_min_password(self):
        professor = {"email": "0123456dasd789@unb.brassasa", "password": "123"}
        expected_status_code = 400
        expected_json = {
            "email": ["The email must be name(matricula)@unb.br"],
            "password": ["Length must be between 8 and 100."],
        }

        response = self.post(professor)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json, expected_json)


class TestEmailVerifyList(TestFlaskBase):
    def get(self, token):
        return self.client.get(url_for("restapi.emailverifylist", token=token))

    def test_api_must_active_user(self):
        student = valid_student_user(self)
        user_db = student_services.get(email=student.get("email"))
        token = auth_services.create_email_token(user_db)

        response = self.get(token)
        self.assertEqual(response.status_code, 302)

    def test_api_must_validate_token(self):
        token = "asdc1a5a1sc6a1ca" * 5
        response = self.get(token)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("message"), "Token invalid")

    def test_api_must_block_no_token(self):
        response = self.get(token=None)
        self.assertEqual(response.status_code, 400)


class TestResendMailVerify(TestFlaskBase):
    def post(self, email):
        return self.client.post(url_for("restapi.emailverifylist"), json=email)

    def test_api_must_resend_mail(self):
        user = valid_student_user(self)

        with self.app.mail.record_messages() as outbox:
            response = self.post({"email": user.get("email")})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(outbox), 1)
            self.assertEqual(outbox[0].recipients, [user.get("email")])

    def test_api_must_not_resent_email_when_user_is_actived(self):
        user = valid_student_user(self)
        user_db = student_services.get(email=user.get("email"))
        user_db.active_user()
        user_db.save_changes()

        response = self.post({"email": user.get("email")})

        self.assertEqual(response.status_code, 203)
        self.assertEqual(response.json.get("message"), "User's e-mail already verified")

    def test_api_must_validate_email(self):
        email = {"email": "123456789@gmail.com"}
        response = self.post(email)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json.get("email"))

    def test_api_must_validate_user_not_found(self):
        email = {"email": "190020377@aluno.unb.br"}
        response = self.post(email)
        self.assertEqual(response.status_code, 404)
