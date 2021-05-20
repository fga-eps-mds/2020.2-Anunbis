from . import ma
from marshmallow import fields, validate
from ..model import report


class ReportSchema(ma.SQLAlchemySchema):
    class Meta:
        model = report.Report

    id_post = fields.Integer(required=True, validate=validate.Range(min=0))
    content = fields.String(required=True, validate=validate.Length(min=10, max=120))
    offensive = fields.Boolean(required=True)
    prejudice = fields.Boolean(required=True)
    unrelated = fields.Boolean(required=True)
    others = fields.Boolean(required=True)
