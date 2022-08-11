from app.schemas.professor_schema import ProfessorSchema
from app.schemas.user_schema import ValidateEmail
import unittest


class TestSchemaProfessor(unittest.TestCase):

    def test_is_validate_name_1(self):
        try:
            ProfessorSchema().validate_name("Lameque")
        except:
            self.assertTrue(False)

    def test_is_validate_name_2(self):
        try:
            ProfessorSchema().validate_name("Lameque Fernandes Azevedo")
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
            ProfessorSchema().validate_name("lameque fernandes")
        except:
            self.assertTrue(False)

    def test_is_validate_name_5(self):
        try:
            ProfessorSchema().validate_name("asdasdasd asdadasdasd asdasd")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def test_is_validate_name_6(self):
        try:
            ProfessorSchema().validate_name("asdasdasdasdadasdasdasdasd")
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_is_validate_name_7(self):
        try:
            ProfessorSchema().validate_name(" ")
            self.assertTrue(True)
        except:
            self.assertTrue(False)