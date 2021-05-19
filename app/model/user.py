from ..ext.database import db
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    __abstract__ = True

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=True, unique=True)
    __email_verified = db.Column(
        "email_verified", db.Boolean, nullable=False, default=False
    )
    __password_hash = db.Column("password", db.String(255))

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.__password_hash = pbkdf2_sha256.hash(password)

    def is_professor(self):
        raise NotImplementedError

    def is_verified(self):
        return self.__email_verified

    def active_user(self):
        self.__email_verified = True

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.__password_hash)

    def save_changes(self):
        db.session.commit()

    def clean(self):
        self.email = None
        self.__email_verified = False
        self.__password_hash = None
