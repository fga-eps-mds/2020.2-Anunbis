from .discipline import Discipline


class Course:
    def __init__(self, id_course=None, name=None, disciplines=None, course_bd=None):
        if course_bd:
            id_course, name = self.__create_from_db(course_bd)

        self.id_course = id_course
        self.name = name
        self.disciplines = disciplines

    def __create_from_db(self, course_bd):
        id_couse = course_bd.id_course
        name = course_bd.name
        return id_couse, name

    def set_disciplines_from_db(self, disciplines_bd):
        self.disciplines = [Discipline(discipline_bd=discipline_bd) for discipline_bd in disciplines_bd]

    @property
    def id_course(self):
        return self.__id_course

    @id_course.setter
    def id_course(self, id_course):
        self.__id_course = id_course

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def disciplines(self):
        return self.__disciplines

    @disciplines.setter
    def disciplines(self, value):
        if value:
            self.__disciplines = value
        else:
            self.__disciplines = []
