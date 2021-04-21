from . import ma, post_schema, discipline_schema
from marshmallow import fields, validates, validate, ValidationError
from re import match
from ..model.professor import Professor


class ProfessorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professor
        additional = ['rating']

    id_professor = fields.Integer()
    reg_professor = fields.Integer(required=True, validate=validate.Range(min=10000000000, max=99999999999))
    name = fields.String(required=True, validate=validate.Length(min=2, max=254))
    password = fields.String(required=True, validate=validate.Length(min=8, max=100), load_only=True)
    email = fields.Email(required=True)

    posts = fields.List(fields.Nested(post_schema.PostSchema(exclude=['discipline_code', 'reg_student'])))
    disciplines = fields.List(fields.Nested(discipline_schema.DisciplineSchema))

    @validates("email")
    def validate_email(self, value):
        if len(value) > 100:
            raise ValidationError("The email must be lower than 100")
        elif not match("[a-z . 0-9]+@unb.br", value.lower()):
            raise ValidationError("The email must be name(matricula)@unb.br")
