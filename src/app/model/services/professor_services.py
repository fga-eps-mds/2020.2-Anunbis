from ..dao import professor_dao


def get_professor_reg(reg_professor):
    professor = professor_dao.Professor.query.filter_by(reg_professor=reg_professor).first()
    return professor

