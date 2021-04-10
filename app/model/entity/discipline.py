from .professor import Professor


class Discipline:
    def __init__(self, discipline_code=None, name=None, professors=None, courses=None, discipline_bd=None):
        if discipline_bd:
            discipline_code, name = self.__create_from_db(discipline_bd)

        self.__discipline_code = discipline_code
        self.__name = name
        self.__professors = professors
        self.__courses = courses

    def __create_from_db(self, discipline_bd):
        discipline_code = discipline_bd.discipline_code
        name = discipline_bd.name
        return discipline_code, name

    def set_professors_from_db(self, professors_db):
        self.professors = [Professor(professor_bd=professor_bd) for professor_bd in professors_db]

    @property
    def discipline_code(self):
        return self.__discipline_code

    @discipline_code.setter
    def discipline_code(self, value):
        self.__discipline_code = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def professors(self):
        return self.__professors

    @professors.setter
    def professors(self, value):
        self.__professors = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.__courses = value
