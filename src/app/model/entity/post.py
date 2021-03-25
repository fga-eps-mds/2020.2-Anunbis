

class Post:
    def __init__(self, reg_student, id_professor, discipline_code, content, rating, is_anonymous):
        self.__id_post = None
        self.__reg_student = reg_student
        self.__id_professor = id_professor
        self.__discipline_code = discipline_code
        self.__content = content
        self.__post_date = None
        self.__rating = rating
        self.__is_anonymous = is_anonymous
        self.__agrees = None
        self.__disagrees = None

    @property
    def id_post(self):
        return self.__id_post

    @id_post.setter
    def id_post(self, value):
        self.__id_post = value

    @property
    def reg_student(self):
        return self.__reg_student

    @reg_student.setter
    def reg_student(self, value):
        self.__id_professor = value

    @property
    def id_professor(self):
        return self.__id_professor

    @id_professor.setter
    def id_professor(self, value):
        self.__id_professor = value

    @property
    def discipline_code(self):
        return self.__discipline_code

    @discipline_code.setter
    def discipline_code(self, value):
        self.__discipline_code = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def post_date(self):
        return self.__post_date

    @post_date.setter
    def post_date(self, value):
        self.__post_date = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def is_anonymous(self):
        return self.__is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value):
        self.__is_anonymous = value

    @property
    def agrees(self):
        return self.__agrees

    @agrees.setter
    def agrees(self, value):
        self.__agrees = value

    @property
    def disagrees(self):
        return self.__disagrees

    @disagrees.setter
    def disagrees(self, value):
        self.__disagrees = value

