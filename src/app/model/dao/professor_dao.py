from ...ext.database import db
from passlib.hash import pbkdf2_sha256


class Professor(db.Model):
    __tablename__ = "PROFESSOR"

    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reg_professor = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, default='')
    password = db.Column(db.String(255), nullable=False, default='')
    disciplines = db.relationship('Discipline', secondary='PROFESSOR_DISCIPLINE', lazy='dynamic')

    posts = db.relationship('Post', back_populates="professor")

    def generate_password(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

    @property
    def rating(self):
        if len(self.posts) is 0:
            return

        soma = 0
        for post in self.posts:
            soma += post.rating
        return soma / len(self.posts)