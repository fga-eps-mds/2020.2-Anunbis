from ..ext.database import db
from .user import User


class Student(User):
    __tablename__ = "student"

    reg_student = db.Column(db.Integer, nullable=False, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    id_course = db.Column(db.Integer, db.ForeignKey("course.id_course"), nullable=False)
    course = db.relationship("Course")

    posts = db.relationship("Post", viewonly=True)
    post_agrees = db.relationship("Post", viewonly=True)
    post_disagrees = db.relationship("Post", viewonly=True)

    @property
    def reg(self):
        return self.reg_student

    def is_professor(self):
        return False

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.reg_student
        else:
            return other.reg == self.reg
