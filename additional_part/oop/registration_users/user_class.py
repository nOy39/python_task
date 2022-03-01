class User:
    def __init__(self, user_name, user_password, user_email):
        from random import randrange
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_id = randrange(0, 999999999)

    def get_user_name(self):
        return self.user_name

    def get_user_password(self):
        return self.user_password


