from . import ma
from marshmallow import fields
from app.models import course_model


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = course_model.Course

    id_course = fields.Integer(required=True)
    name = fields.String(required=True)
