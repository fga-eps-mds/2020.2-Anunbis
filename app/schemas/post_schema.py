from . import ma, discipline_schema, student_schema
from marshmallow import fields, validate
from ..model import post


class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = post.Post

    id_post = fields.Integer(required=True, validate=validate.Range(min=0))
    reg_student = fields.Integer(
        required=True, validate=validate.Range(min=0), load_only=True
    )
    id_professor = fields.Integer(required=True, validate=validate.Range(min=0))
    discipline_code = fields.String(
        required=True, validate=validate.Length(max=80), load_only=True
    )
    content = fields.String(required=True, validate=validate.Length(min=1, max=480))
    didactic = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    metod = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    avaliations = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    disponibility = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    is_anonymous = fields.Boolean(required=True)
    post_date = fields.Date()
    rating = fields.Float()
    discipline = fields.Nested(discipline_schema.DisciplineSchema)
    student = fields.Method("gen_student")
    feedbacks = fields.Method("gen_feedbacks")

    def gen_feedbacks(self, obj):
        is_agreed = False
        is_disagreed = False

        if self.context.get("reg_student"):
            reg_student = int(self.context["reg_student"])
            is_agreed = reg_student in obj.agrees
            is_disagreed = reg_student in obj.disagrees

        return {
            "agrees": len(obj.agrees),
            "disagrees": len(obj.disagrees),
            "is_agreed": is_agreed,
            "is_disagreed": is_disagreed,
        }

    def gen_student(self, obj):
        if obj.is_anonymous:
            return student_schema.StudentSchema(only=["course"]).dump(obj.student)
        else:
            return student_schema.StudentSchema(only=["course", "name"]).dump(
                obj.student
            )
