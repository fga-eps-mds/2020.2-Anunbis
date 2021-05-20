from ..ext.database import db


class ProfessorDiscipline(db.Model):
    __tablename__ = "professor_discipline"

    discipline_code = db.Column(
        db.String(80),
        db.ForeignKey("discipline.discipline_code"),
        nullable=False,
        primary_key=True,
    )

    id_professor = db.Column(
        db.Integer,
        db.ForeignKey("professor.id_professor"),
        nullable=False,
        primary_key=True,
    )


class Discipline(db.Model):
    __tablename__ = "discipline"

    discipline_code = db.Column(
        db.String(80), nullable=False, default="", primary_key=True
    )
    name = db.Column(db.String(255), nullable=False, default="")
    courses = db.relationship("Course", secondary="course_discipline", lazy="dynamic")
