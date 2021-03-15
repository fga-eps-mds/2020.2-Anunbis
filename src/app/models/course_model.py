from ..ext.database import db

COUSE_DISCIPLINE = db.Table('COUSE_DISCIPLINE',
                            db.Column('discipline_code', db.String(80), db.ForeignKey('DISCIPLINE.discipline_code'),
                                      nullable=False, primary_key=True),
                            db.Column('id_course', db.Integer, db.ForeignKey('COUSE.id_course'), nullable=False,
                                      primary_key=True))


class Course(db.Model):
    __tablename__ = "COURSE"

    id_course = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    disciplines = db.relationship('DISCIPLINE', secondary=COUSE_DISCIPLINE, lazy='dynamic', back_populates='professors')
