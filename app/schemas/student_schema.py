from . import ma, course_schema
from marshmallow import fields, validates, validate
from ..model.student import Student
from .user_schema import ValidateEmail


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student

    reg_student = fields.Integer(
        required=True, validate=validate.Range(min=100000000, max=999999999)
    )
    name = fields.String(required=True, validate=validate.Length(min=2, max=254))
    id_course = fields.Integer(required=True, validate=validate.Range(min=0))
    password = fields.String(
        required=True, validate=validate.Length(min=8, max=100), load_only=True
    )
    email = fields.Email(required=True)

    course = fields.Nested(course_schema.CourseSchema)

    @validates("email")
    def validate_email(self, value):
        ValidateStudentEmail().validate(value)


class ValidateStudentEmail(ValidateEmail):
    def validate(self, value):
        self.validate_length(value)
        self.validate_format(
            value, "[0-9]+@aluno.unb.br$", "The email must be matricula@aluno.unb.br"
        )
