from ...ext.database import db

PROFESSOR_DISCIPLINE = db.Table('PROFESSOR_DISCIPLINE',
                                db.Column('discipline_code', db.String(80), db.ForeignKey('DISCIPLINE.discipline_code'),
                                          nullable=False, primary_key=True),
                                db.Column('id_professor', db.Integer, db.ForeignKey('PROFESSOR.id_professor'),
                                          nullable=False, primary_key=True))


class Discipline(db.Model):
    __tablename__ = "DISCIPLINE"

    discipline_code = db.Column(db.String(80), nullable=False, default='', primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    professors = db.relationship('Professor', secondary=PROFESSOR_DISCIPLINE, lazy='dynamic')
    courses = db.relationship('Course', secondary='COURSE_DISCIPLINE', lazy='dynamic')
