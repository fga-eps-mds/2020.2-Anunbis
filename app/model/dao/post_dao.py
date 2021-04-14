from ...ext.database import db
from datetime import date
from . import professor_dao
from datetime import datetime, date

class DisagreeStudentPost(db.Model):
    __tablename__ = "disagree_student_post"
    
    id_post = db.Column('id_post', db.Integer, db.ForeignKey('post.id_post'), nullable=False, primary_key=True)
    reg_student = db.Column('reg_student', db.Integer, db.ForeignKey('student.reg_student'), nullable=False, primary_key=True)

class AgreeStudentPost(db.Model):
    __tablename__ = "agree_student_post"
    
    id_post = db.Column('id_post', db.Integer, db.ForeignKey('post.id_post'), nullable=False, primary_key=True)
    reg_student = db.Column('reg_student', db.Integer, db.ForeignKey('student.reg_student'), nullable=False, primary_key=True)


class Post(db.Model):
    __tablename__ = "post"

    id_post = db.Column(db.Integer, nullable=False, primary_key=True)
    post_date = db.Column(db.Date, default = date.today(), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(480), nullable=False)
    is_anonymous = db.Column(db.Boolean, nullable=False)

    discipline_code = db.Column(db.Integer, db.ForeignKey('discipline.discipline_code'), nullable=False)
    discipline = db.relationship('Discipline')

    reg_student = db.Column(db.Integer, db.ForeignKey('student.reg_student'), nullable=False)
    student = db.relationship('Student', back_populates='posts')

    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id_professor'), nullable=False)
    professor = db.relationship(professor_dao.Professor, back_populates="posts")

    agrees = db.relationship('Student', secondary="agree_student_post")
    disagrees = db.relationship('Student', secondary="agree_student_post")
    
    @staticmethod
    def delete(post_db):
        Post.delete_feedbacks(post_db)
        Post.delete_reports(post_db)
        db.session.delete(post_db)
        db.session.commit()

    @staticmethod
    def delete_feedbacks(post_db):
        for agree in AgreeStudentPost.query.filter_by(id_post=post_db.id_post).all():
            db.session.delete(agree)
        for disagree in DisagreeStudentPost.query.filter_by(id_post=post_db.id_post).all():
            db.session.delete(disagree)
        db.session.commit()

    def delete_reports(post_db):
        pass