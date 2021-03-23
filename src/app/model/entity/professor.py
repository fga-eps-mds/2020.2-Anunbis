

class professor:
    def __init__(self, reg_professor, name, email, password):
        self.__reg_professor = reg_professor
        self.__name = name
        self.__email = email
        self.__password = password
        self.__post_agrees = None
        self.__post_disagrees = None

    @property
    def reg_professor(self):
        return self.__reg_professor

    @reg_professor.setter
    def reg_professor(self, reg_professor):
        self.__reg_professor = reg_professor

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
