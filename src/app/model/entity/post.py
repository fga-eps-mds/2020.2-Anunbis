

class Post:
    def __init__(self, reg_student, reg_professor, discipline_code, content, rating, is_anonymous):
        self.id_post = None
        self.reg_student = reg_student
        self.reg_professor = reg_professor
        self.discipline_code = discipline_code
        self.content = content
        self.post_date = None
        self.rating = rating
        self.is_anonymous = is_anonymous
        self.agrees = None
        self.disagrees = None

    @property
    def id_post(self):
        return self.id_post

    @id_post.setter
    def id_post(self, value):
        self.id_post = value

    @property
    def reg_student(self):
        return self.reg_student

    @reg_student.setter
    def reg_student(self, value):
        self.reg_professor = value

    @property
    def reg_professor(self):
        return self.reg_professor

    @reg_professor.setter
    def reg_professor(self, value):
        self.reg_professor = value

    @property
    def discipline_code(self):
        return self.discipline_code

    @discipline_code.setter
    def discipline_code(self, value):
        self.discipline_code = value

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        self.content = value

    @property
    def post_date(self):
        return self.post_date

    @post_date.setter
    def post_date(self, value):
        self.post_date = value

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, value):
        self.rating = value

    @property
    def is_anonymous(self):
        return self.is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value):
        self.is_anonymous = value

    @property
    def agrees(self):
        return self.agrees

    @agrees.setter
    def agrees(self, value):
        self.agrees = value

    @property
    def disagrees(self):
        return self.disagrees

    @disagrees.setter
    def disagrees(self, value):
        self.disagrees = value

