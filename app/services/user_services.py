from ..services import professor_services, student_services


def is_professor(email=None, reg=None):
    return len(str(reg)) == 11 if reg else "aluno" not in email.lower()


def get(reg=None, email=None):
    if is_professor(reg=reg, email=email):
        return __get_professor(reg, email)
    else:
        return __get_student(reg, email)


def __get_professor(reg, email):
    if reg:
        return professor_services.get(reg_professor=reg)
    else:
        return professor_services.get_by_email(email=email)


def __get_student(reg, email):
    if reg:
        return student_services.get(reg_student=reg)
    else:
        return student_services.get_by_email(email=email)
