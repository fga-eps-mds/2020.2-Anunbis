from ..ext.database import db
from .discipline import Discipline

COURSE_DISCIPLINE = db.Table(
    "course_discipline",
    db.Column(
        "discipline_code",
        db.String(80),
        db.ForeignKey(Discipline.discipline_code),
        nullable=False,
        primary_key=True,
    ),
    db.Column(
        "id_course",
        db.Integer,
        db.ForeignKey("course.id_course"),
        nullable=False,
        primary_key=True,
    ),
)


class Course(db.Model):
    __tablename__ = "course"

    id_course = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default="")
    disciplines = db.relationship(
        Discipline, secondary=COURSE_DISCIPLINE, lazy="dynamic"
    )
