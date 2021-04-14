

class Student:
    def __init__(self, reg_student=None, name=None, email=None, password=None, id_course=None, post_agrees=None, post_disagrees=None):
        self.reg_student = reg_student
        self.name = name
        self.email = email
        self.password = password
        self.id_course = id_course
        self.post_agrees = post_agrees
        self.post_disagrees = post_disagrees

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
        self.__name = name

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
