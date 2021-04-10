from . import ma
from marshmallow import fields
from ..model.dao import discipline_dao


class DisciplineSchema(ma.SQLAlchemySchema):
    class Meta:
        model = discipline_dao.Discipline

    discipline_code = fields.String()
    name = fields.String()