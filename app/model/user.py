from ..model.student import Student
from ..model.professor import Professor
from sqlalchemy import func


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_professor(self):
        return is_professor(email=self.email)

    def get(self):
        return get(email=self.email)


def is_professor(email=None, reg=None):
    return len(str(reg)) == 11 if reg else "aluno" not in email.lower()


def get(reg=None, email=None):
    if is_professor(reg=reg, email=email):
        if reg:
            return Professor.query.filter_by(reg_professor=reg).one_or_none()
        return Professor.query.filter(
            func.lower(Professor.email) == email.lower()
        ).one_or_none()
    else:
        if reg:
            return Student.query.filter_by(reg_student=reg).one_or_none()
        else:
            return Student.query.filter(
                func.lower(Student.email) == email.lower()
            ).one_or_none()
