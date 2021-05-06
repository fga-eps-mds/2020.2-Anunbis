from . import ma
from marshmallow import fields
from ..model.discipline import Discipline


class DisciplineSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Discipline

    discipline_code = fields.String()
    name = fields.String()
