from ..ext.database import db
from .discipline_model import Discipline

COURSE_DISCIPLINE = db.Table('COURSE_DISCIPLINE',
                            db.Column('discipline_code', db.String(80), db.ForeignKey(Discipline.discipline_code),
                                      nullable=False, primary_key=True),
                            db.Column('id_course', db.Integer, db.ForeignKey('COURSE.id_course'), nullable=False,
                                      primary_key=True))


class Course(db.Model):
    __tablename__ = "COURSE"

    id_course = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    disciplines = db.relationship(Discipline, secondary=COURSE_DISCIPLINE, lazy='dynamic')
