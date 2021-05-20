from ..ext.database import db
from datetime import date


class DisagreeStudentPost(db.Model):
    __tablename__ = "disagree_student_post"

    id_post = db.Column(
        "id_post",
        db.Integer,
        db.ForeignKey("post.id_post"),
        nullable=False,
        primary_key=True,
    )
    reg_student = db.Column(
        "reg_student",
        db.Integer,
        db.ForeignKey("student.reg_student"),
        nullable=False,
        primary_key=True,
    )


class AgreeStudentPost(db.Model):
    __tablename__ = "agree_student_post"

    id_post = db.Column(
        "id_post",
        db.Integer,
        db.ForeignKey("post.id_post"),
        nullable=False,
        primary_key=True,
    )
    reg_student = db.Column(
        "reg_student",
        db.Integer,
        db.ForeignKey("student.reg_student"),
        nullable=False,
        primary_key=True,
    )


class Post(db.Model):
    __tablename__ = "post"

    id_post = db.Column(
        db.Integer, nullable=False, primary_key=True, autoincrement=True
    )
    post_date = db.Column(db.Date, default=date.today(), nullable=False)
    didactic = db.Column(db.SmallInteger, nullable=False)
    metod = db.Column(db.SmallInteger, nullable=False)
    avaliations = db.Column(db.SmallInteger, nullable=False)
    disponibility = db.Column(db.SmallInteger, nullable=False)
    content = db.Column(db.String(480), nullable=False)
    is_anonymous = db.Column(db.Boolean, nullable=False)

    discipline_code = db.Column(
        db.String(80), db.ForeignKey("discipline.discipline_code"), nullable=False
    )
    discipline = db.relationship("Discipline")

    reg_student = db.Column(
        db.Integer, db.ForeignKey("student.reg_student"), nullable=False
    )
    student = db.relationship("Student", back_populates="posts")

    id_professor = db.Column(
        db.Integer, db.ForeignKey("professor.id_professor"), nullable=False
    )
    professor = db.relationship("Professor", back_populates="posts")

    agrees = db.relationship(
        "Student", secondary="agree_student_post", back_populates="post_agrees"
    )
    disagrees = db.relationship(
        "Student", secondary="disagree_student_post", back_populates="post_disagrees"
    )

    @property
    def rating(self):
        sum = 0
        sum += self.didactic
        sum += self.metod
        sum += self.avaliations
        sum += self.disponibility
        return sum / 4
