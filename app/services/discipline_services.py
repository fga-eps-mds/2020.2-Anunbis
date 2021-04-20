from ..model.discipline import Discipline


def get_discipline_code(discipline_code):
    discipline = Discipline.query.filter_by(discipline_code=discipline_code).first()
    return discipline

