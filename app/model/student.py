from ..ext.database import db
from passlib.hash import pbkdf2_sha256


class Student(db.Model):
    __tablename__ = "student"

    reg_student = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    __password_hash = db.Column("password", db.String(255), nullable=False)

    id_course = db.Column(db.Integer, db.ForeignKey("course.id_course"), nullable=False)
    course = db.relationship("Course")

    posts = db.relationship("Post")
    post_agrees = db.relationship("Post", secondary="agree_student_post")
    post_disagrees = db.relationship("Post", secondary="disagree_student_post")

    @property
    def reg(self):
        return self.reg_student

    def is_professor(self):
        return False

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.__password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.__password_hash)

    @staticmethod
    def get(**kwargs):
        return Student.query.filter_by(**kwargs).first()

    @staticmethod
    def delete(student_bd):
        Student.delete_feedbacks(student_bd)
        Student.delete_posts(student_bd)
        db.session.delete(student_bd)
        db.session.commit()

    @staticmethod
    def delete_posts(student_bd):
        from .post import Post

        for post in student_bd.posts:
            Post.delete(post)

    @staticmethod
    def delete_feedbacks(student_bd):
        from .post import AgreeStudentPost, DisagreeStudentPost

        for agree in AgreeStudentPost.query.filter_by(
            reg_student=student_bd.reg_student
        ).all():
            db.session.delete(agree)
        for disagree in DisagreeStudentPost.query.filter_by(
            reg_student=student_bd.reg_student
        ).all():
            db.session.delete(disagree)
        db.session.commit()

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.reg_student
        else:
            return other.reg_student == self.reg_student
