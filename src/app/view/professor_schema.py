from . import ma, post_schema
from ..model.dao import professor_dao
from marshmallow import fields


class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_dao.Professor
        additional = ['rating']

    posts = fields.List(fields.Nested(post_schema.PostSchema))
