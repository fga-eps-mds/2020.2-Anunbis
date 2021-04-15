

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_professor(self):
        return not "aluno" in self.email.lower()