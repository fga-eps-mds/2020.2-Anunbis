from ..model.discipline import Discipline


def get(**kwargs):
    return Discipline.query.filter_by(**kwargs).first()
