from ...ext.database import db
from datetime import date
from . import professor_dao

DISAGREE_STUDENT_POST = db.Table('DISAGREE_STUDENT_POST',
                                 db.Column('id_post', db.Integer, db.ForeignKey('POST.id_post'),
                                           nullable=False, primary_key=True),
                                 db.Column('reg_student', db.Integer,
                                           db.ForeignKey('STUDENT.reg_student'), nullable=False, primary_key=True))

AGREE_STUDENT_POST = db.Table('AGREE_STUDENT_POST',
                              db.Column('id_post', db.Integer, db.ForeignKey('POST.id_post'),
                                        nullable=False, primary_key=True),
                              db.Column('reg_student', db.Integer, db.ForeignKey('STUDENT.reg_student'),
                                        nullable=False, primary_key=True))


class Post(db.Model):
    __tablename__ = "POST"

    id_post = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    reg_student = db.Column(db.Integer, db.ForeignKey('STUDENT.reg_student'), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('PROFESSOR.id_professor'), nullable=False)
    content = db.Column(db.String(480), nullable=False)
    post_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    is_anonymous = db.Column(db.Boolean, nullable=False)
    discipline_code = db.Column(db.Integer, db.ForeignKey('DISCIPLINE.discipline_code'), nullable=False)

    agrees = db.relationship('Student', secondary=AGREE_STUDENT_POST, lazy='dynamic')
    disagrees = db.relationship('Student', secondary=DISAGREE_STUDENT_POST, lazy='dynamic')
    professor = db.relationship(professor_dao.Professor, back_populates="posts")

    def gen_date(self):
        self.post_date = date.today().isoformat()

