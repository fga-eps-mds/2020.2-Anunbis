from ...ext.database import db
from .professor_dao import Professor

PROFESSOR_DISCIPLINE = db.Table('professor_discipline',
                                db.Column('discipline_code', db.String(80), db.ForeignKey('discipline.discipline_code'),
                                          nullable=False, primary_key=True),
                                db.Column('id_professor', db.Integer, db.ForeignKey('professor.id_professor'),
                                          nullable=False, primary_key=True))


class Discipline(db.Model):
    __tablename__ = "discipline"

    discipline_code = db.Column(db.String(80), nullable=False, default='', primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    professors = db.relationship(Professor, secondary=PROFESSOR_DISCIPLINE, lazy='dynamic')
    courses = db.relationship('Course', secondary='course_discipline', lazy='dynamic')
