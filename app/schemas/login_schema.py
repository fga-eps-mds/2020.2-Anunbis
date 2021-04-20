from . import ma
from marshmallow import fields, validate, validates, ValidationError
from ..model.student import Student
from re import match


class LoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'password']

    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=100))

    @validates("email")
    def validate_email(self, value):
        if len(value) > 100:
            raise ValidationError("The email must be lower than 100")
        elif not match("[0-9]+@aluno.unb.br", value.lower()):
            raise ValidationError("The email must be matricula@aluno.unb.br")