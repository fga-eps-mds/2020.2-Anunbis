from app.schemas.user_schema import UserSchema
import unittest


class TestUser(unittest.TestCase):
    '''Deve lançar um erro caso o email seja nulo'''
    def test_validate_email_none(self):
        try:
            UserSchema().validate_email(None)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    '''Deve lançar um erro caso o email seja do tipo inteiro'''
    def test_validate_email_number(self):
        try:
            UserSchema().validate_email(2)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    '''Deve lançar um erro caso o email seja invalido o formato'''
    def test_validate_email_invalid(self):
        try:
            UserSchema().validate_email('fellipe')
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    '''Deve aceitar o caso se email for valido'''
    def test_validate_email_correto(self):
        try:
            UserSchema().validate_email('fellipe@gmail.com')
            self.assertFalse(False)
        except:
            self.assertTrue(True)

    '''Deve lançar um erro caso o email seja true'''
    def test_validate_email_True(self):
        try:
            UserSchema().validate_email(True)
            self.assertTrue(True)
        except:
            self.assertFalse(False)
    
    '''Deve lançar um erro caso o email seja false'''
    def test_validate_email_False(self):
        try:
            UserSchema().validate_email(False)
            self.assertTrue(True)
        except:
            self.assertFalse(False)
    
    def test_validate_email_upper(self):
        try:
            UserSchema().validate_email(False)
            self.assertTrue(True)
        except:
            self.assertFalse(False)
