from .user import User
from ..ext.database import db


class Professor(User):
    __tablename__ = "professor"

    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reg_professor = db.Column(db.BigInteger, nullable=True, unique=True)
    disciplines = db.relationship(
        "Discipline", secondary="professor_discipline", lazy="dynamic"
    )
    posts = db.relationship("Post", back_populates="professor")

    @property
    def reg(self):
        return self.reg_professor

    @property
    def rating(self):
        if len(self.posts) == 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.rating
        return sum / len(self.posts)

    @property
    def didactic(self):
        if len(self.posts) == 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.didactic
        return sum / len(self.posts)

    @property
    def metod(self):
        if len(self.posts) == 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.metod
        return sum / len(self.posts)

    @property
    def avaliations(self):
        if len(self.posts) == 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.avaliations
        return sum / len(self.posts)

    @property
    def disponibility(self):
        if len(self.posts) == 0:
            return

        sum = 0
        for post in self.posts:
            sum += post.disponibility
        return sum / len(self.posts)

    def is_professor(self):
        return True

    def clean_credentials(self):
        self.clean()
        self.reg_professor = None
