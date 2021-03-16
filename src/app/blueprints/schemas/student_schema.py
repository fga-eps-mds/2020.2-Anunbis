from . import ma
from marshmallow import fields
from app.models import student_model


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = student_model.Student

    reg_student = fields.Integer(required=True)
    name = fields.String(required=True)
    id_course = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
