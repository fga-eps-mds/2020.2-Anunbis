from ...ext.database import db
from passlib.hash import pbkdf2_sha256


class Student(db.Model):
    __tablename__ = 'STUDENT'

    reg_student = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    id_course = db.Column(db.Integer, db.ForeignKey("COURSE.id_course"), nullable=False)
    course = db.relationship('Course')

    post_agrees = db.relationship('Post', secondary='AGREE_STUDENT_POST', lazy='dynamic')
    post_disagrees = db.relationship('Student', secondary='DISAGREE_STUDENT_POST', lazy='dynamic')

    def generate_password(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)


