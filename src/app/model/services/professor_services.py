from ..dao import professor_dao


def get_professor_id(id_professor):
    professor = professor_dao.Professor.query.filter_by(id_professor=id_professor).first()
    return professor

