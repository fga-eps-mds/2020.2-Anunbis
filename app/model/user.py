from ..model import student, professor


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_professor(self):
        return is_professor(email=self.email)

    def get(self):
        return get(email=self.email)


def is_professor(email=None, reg=None):
    return (
        len(str(reg)) == 11
        if reg
        else not "aluno" in email.lower()
    )


def get(reg=None, email=None):
    if is_professor(reg=reg, email=email):
        if reg:
            return professor.Professor.query.filter_by(reg_professor=reg).one_or_none()
        return professor.Professor.query.filter_by(email=email).one_or_none()
    else:
        if reg:
            return student.Student.query.filter_by(reg_student=reg).one_or_none()
        else:
            return student.Student.query.filter_by(email=email).one_or_none()
