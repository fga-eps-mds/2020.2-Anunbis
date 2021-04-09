

class Course:
    def __init__(self, id_course, name, disciplines):
        self.__id_course = id_course
        self.__name = name
        self.__disciplines = disciplines

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
        self.name = name

    @property
    def disciplines(self):
        return self.__disciplines

    @disciplines.setter
    def disciplines(self, disciplines):
        self.__disciplines = disciplines
