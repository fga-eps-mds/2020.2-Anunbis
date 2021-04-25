

class User:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def is_professor(self, reg=None):
        if reg:
            return len(reg) == 11
        return not "aluno" in self.email.lower()
