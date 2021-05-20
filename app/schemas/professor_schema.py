from . import ma, post_schema, discipline_schema
from marshmallow import fields, validates, validate, ValidationError
from ..model.professor import Professor
from .user_schema import ValidateEmail


class ProfessorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professor
        additional = ["rating", "didactic", "metod", "avaliations", "disponibility"]

    id_professor = fields.Integer(validate=validate.Range(min=0))
    reg_professor = fields.Integer(
        required=True, validate=validate.Range(min=10000000000, max=99999999999)
    )
    name = fields.String(required=True, validate=validate.Length(min=2, max=254))
    password = fields.String(
        required=True, validate=validate.Length(min=8, max=100), load_only=True
    )
    email = fields.Email(required=True)

    posts = fields.List(
        fields.Nested(
            post_schema.PostSchema(exclude=["discipline_code", "reg_student"])
        )
    )
    disciplines = fields.List(fields.Nested(discipline_schema.DisciplineSchema))

    @validates("email")
    def validate_email(self, value):
        ValidateProfessorEmail().validate(value)

    @validates("name")
    def validate_name(self, value):
        for char in value:
            if not char.isalpha() and char != " ":
                raise ValidationError("Name should have just letters!")


class ValidateProfessorEmail(ValidateEmail):
    def validate(self, value):
        self.validate_length(value)
        self.validate_format(
            value, "[a-z.0-9]+@unb.br$", "The email must be name(matricula)@unb.br"
        )
