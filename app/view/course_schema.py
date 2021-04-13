from . import ma
from marshmallow import fields
from ..model.entity import course


class CourseSchema(ma.Schema):
    class Meta:
        model = course.Course

    id_course = fields.Integer(required=True)
    name = fields.String(required=True)
