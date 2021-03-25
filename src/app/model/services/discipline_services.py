from ..dao import discipline_dao


def get_discipline_code(discipline_code):
    discipline = discipline_dao.Discipline.query.filter_by(discipline_code=discipline_code)
    return discipline

