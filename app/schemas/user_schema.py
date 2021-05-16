from . import ma
from marshmallow import fields, validate, validates, ValidationError
from ..model.user import User
from re import match


class UserSchema(ma.Schema):
    class Meta:
        model = User

    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=100))

    @validates("email")
    def validate_email(self, value):
        if value.lower().find("aluno") != -1:
            from .student_schema import ValidateStudentEmail

            ValidateStudentEmail().validate(value)
        else:
            from .professor_schema import ValidateProfessorEmail

            ValidateProfessorEmail().validate(value)


class ValidateEmail:
    def validate_length(self, value):
        if len(value) > 100:
            raise ValidationError("The email must be lower than 100")

    def validate_format(self, value, format, error_message):
        if not match(format, value.lower()):
            raise ValidationError(error_message)
