from . import ma
from marshmallow import fields
from ..model.course import Course


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Course

    id_course = fields.Integer(required=True)
    name = fields.String(required=True)
