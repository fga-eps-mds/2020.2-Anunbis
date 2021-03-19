from . import ma
from marshmallow import fields
from ..model.dao import course_dao


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = course_dao.Course

    id_course = fields.Integer(required=True)
    name = fields.String(required=True)
