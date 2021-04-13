from ...ext.database import db
from datetime import date
from . import professor_dao
from datetime import datetime, date

DISAGREE_STUDENT_POST = db.Table('disagree_student_post',
                                 db.Column('id_post', db.Integer, db.ForeignKey('post.id_post'),
                                           nullable=False, primary_key=True),
                                 db.Column('reg_student', db.Integer,
                                           db.ForeignKey('student.reg_student'), nullable=False, primary_key=True))

AGREE_STUDENT_POST = db.Table('agree_student_post',
                              db.Column('id_post', db.Integer, db.ForeignKey('post.id_post'),
                                        nullable=False, primary_key=True),
                              db.Column('reg_student', db.Integer, db.ForeignKey('student.reg_student'),
                                        nullable=False, primary_key=True))


class Post(db.Model):
    __tablename__ = "post"

    id_post = db.Column(db.Integer, nullable=False, primary_key=True)
    reg_student = db.Column(db.Integer, db.ForeignKey('student.reg_student'), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id_professor'), nullable=False)
    content = db.Column(db.String(480), nullable=False)
    post_date = db.Column(db.Date, default = date.today(), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    is_anonymous = db.Column(db.Boolean, nullable=False)

    discipline_code = db.Column(db.Integer, db.ForeignKey('discipline.discipline_code'), nullable=False)
    discipline = db.relationship('Discipline')

    reg_student = db.Column(db.Integer, db.ForeignKey('student.reg_student'), nullable=False)
    student = db.relationship('Student')

    agrees = db.relationship('Student', secondary=AGREE_STUDENT_POST, lazy='dynamic')
    disagrees = db.relationship('Student', secondary=DISAGREE_STUDENT_POST, lazy='dynamic')
    professor = db.relationship(professor_dao.Professor, back_populates="posts")

    professor = db.relationship(professor_dao.Professor, back_populates="posts")
