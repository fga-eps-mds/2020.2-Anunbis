from ..ext.database import db

PROFESSOR_DISCIPLINE = db.Table('PROFESSOR_DISCIPLINE',
                                db.Column('discipline_code', db.String(80), db.ForeignKey('DISCIPLINE.discipline_code'),
                                          nullable=False, primary_key=True),
                                db.Column('reg_professor', db.Integer, db.ForeignKey('PROFESSOR.reg_professor'),
                                          nullable=False, primary_key=True))


class Discipline(db.Model):
    __tablename__ = "DISCIPLINE"

    discipline_code = db.Column(db.String(80), nullable=False, default='', primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    professors = db.relationship('PROFESSOR', secondary=PROFESSOR_DISCIPLINE, lazy='dynamic',
                                 back_populates='disciplines')
    courses = db.relationship('COURSE', secondary='COUSE_DISCIPLINE', lazy='dynamic', back_populates='disciplines')
