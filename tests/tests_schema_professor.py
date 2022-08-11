from app.schemas.professor_schema import ProfessorSchema
from app.schemas.user_schema import ValidateEmail
import unittest


class TestSchemaProfessor(unittest.TestCase):

    # Teste em SCHAMA DE PROFESSOR

    def test_is_validate_name_1(self):
        try:
            ProfessorSchema().validate_name("Lameque")
        except:
            self.assertTrue(False)

    def test_is_validate_name_2(self):
        try:
            ProfessorSchema().validate_name("Lameque100")
        except:
            self.assertTrue(False)
    
    def test_is_validate_name_3(self):
        try:
            ProfessorSchema().validate_name("Lameque Fernandes")
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_is_validate_name_4(self):
        try:
            ProfessorSchema().validate_name("Lameque Fernandes 1000")
        except:
            self.assertTrue(False)

    def test_is_validate_name_5(self):
        try:
            ProfessorSchema().validate_name("1000")
            self.assertTrue(True)
        except:
            self.assertTrue(False)


    # Teste em SCHAMA DE USER

    def test_validate_length_1(self):
        try:
            email = "lamequesao@gmail.com"
            ValidateEmail().validate_length(email)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_validate_length_2(self):
        try:
            string = "1" * 100
            ValidateEmail().validate_length(string)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_validate_length_3(self):
        try:
            string = "1" * 101
            ValidateEmail().validate_length(string)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_validate_length_4(self):
        try:
            string = "1" * 99
            ValidateEmail().validate_length(string)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_validate_length_5(self):
        try:
            string = "1" * 98
            ValidateEmail().validate_length(string)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

