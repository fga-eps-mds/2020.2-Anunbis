from ..services import user_services


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_professor(self):
        return user_services.is_professor(email=self.email)

    def get(self):
        return user_services.get(email=self.email)
