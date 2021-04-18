from . import ma, course_schema
from marshmallow import fields, Schema, validates, validate, ValidationError
from re import match
from ..model.student import Student


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student

    reg_student = fields.Integer(required=True, validate=validate.Range(min=0))            
    name = fields.String(required=True, validate=validate.Length(min=2,max=254))
    id_course = fields.Integer(required=True, validate=validate.Range(min=0))    
    password = fields.String(required=True, validate=validate.Length(min=8, max=100), load_only=True)
    email = fields.Email(required=True)

    course = fields.Nested(course_schema.CourseSchema)

    @validates("email")
    def validate_email(self, value):
        if len(value)>100:
            raise ValidationError("The email must be lower than 100")
        elif not match("[0-9]+@aluno.unb.br",value.lower()):
            raise ValidationError("The email must be matricula@aluno.unb.br")
