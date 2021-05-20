from ..ext.database import db


class CourseDiscipline(db.Model):
    __tablename__ = "course_discipline"

    discipline_code = db.Column(
        db.String(80),
        db.ForeignKey("discipline.discipline_code"),
        nullable=False,
        primary_key=True,
    )
    id_course = db.Column(
        db.Integer,
        db.ForeignKey("course.id_course"),
        nullable=False,
        primary_key=True,
    )


class Course(db.Model):
    __tablename__ = "course"

    id_course = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
