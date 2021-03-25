from . import ma, post_schema
from marshmallow import fields, Schema, validates, validate, ValidationError
from re import match
from ..model.dao import professor_dao

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_dao.Professor
        additional = ['rating']

    id_professor = fields.Integer()
    reg_professor = fields.Integer(required=True, validate=validate.Range(min=0))
    name = fields.String(required=True, validate=validate.Length(min=2,max=254))
    password = fields.String(required=True, validate= validate.Length(min=8, max=100))
    email = fields.Email(required=True)

    posts = fields.List(fields.Nested(post_schema.PostSchema(exclude=['discipline_code', 'reg_student'])))
    disciplines = fields.List(fields.Nested(discipline_schema.DisciplineSchema))
    
    @validates("email")
    def validate_email(self, value):
        if len(value)>100:
            raise ValidationError("The email must be lower than 100")
        elif not match("[a-z . 0-9]+@unb.br",value.lower()):
            raise ValidationError("The email must be name(matricula)@unb.br")
    