from ..ext.database import db
from passlib.hash import pbkdf2_sha256


class Student(db.Model):
    __tablename__ = "student"

    reg_student = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    __password_hash = db.Column("password", db.String(255), nullable=False)

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

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.__password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.__password_hash)

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.reg_student
        else:
            return other.reg_student == self.reg_student
