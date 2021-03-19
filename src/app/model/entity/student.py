

class Student:
    def __init__(self, reg_student, name, email, password, id_course):
        self.__reg_student = reg_student
        self.__name = name
        self.__email = email
        self.__password = password
        self.__id_course = id_course
        self.__post_agrees = None
        self.__post_disagrees = None

    @property
    def reg_student(self):
        return self.__reg_student

    @reg_student.setter
    def reg_student(self, reg_student):
        self.__reg_student = reg_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def id_course(self):
        return self.__id_course

    @id_course.setter
    def id_course(self, id_course):
        self.__id_course = id_course

    @property
    def post_agrees(self):
        return self.__post_agrees

    @post_agrees.setter
    def post_agrees(self, post_agrees):
        self.__post_agrees = post_agrees

    @property
    def post_disagrees(self):
        return self.__post_disagrees

    @post_disagrees.setter
    def post_disagrees(self, post_disagrees):
        self.__post_disagrees = post_disagrees
