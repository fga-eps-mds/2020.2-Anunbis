from ..ext.database import db
from passlib.hash import pbkdf2_sha256


class Professor(db.Model):
    __tablename__ = "professor"

    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reg_professor = db.Column(db.Integer, nullable=True, unique=True)

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True, unique=True)
    __password_hash = db.Column('password', db.String(255), nullable=True)

    disciplines = db.relationship('Discipline', secondary='professor_discipline', lazy='dynamic')

    posts = db.relationship('Post', back_populates="professor")

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.__password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.__password_hash)

    @property
    def rating(self):
        if len(self.posts) is 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.rating
        return sum / len(self.posts)
