from . import ma, discipline_schema, student_schema
from marshmallow import fields, validate
from ..model.dao import post_dao


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = post_dao.Post

    reg_student = fields.Integer(required=True, validate=validate.Range(min=0))
    id_professor = fields.Integer(required=True, validate=validate.Range(min=0))
    discipline_code = fields.String(required=True, validate=validate.Length(max=80))
    content = fields.String(required=True, validate=validate.Length(min=1, max=480))
    rating = fields.Float(required=True, validate=validate.Range(min=0, max=10))
    is_anonymous = fields.Boolean(required=True)
    post_date = fields.Date()

    discipline = fields.Nested(discipline_schema.DisciplineSchema)
    student = fields.Method("gen_student")

    def gen_student(self, obj):
        if obj.is_anonymous:
            return student_schema.StudentSchema(only=['course']).dump(obj.student)
        else:
            return student_schema.StudentSchema(only=['course', 'name']).dump(obj.student)
