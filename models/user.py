# models/user.py
class User:
    def __init__(self, user_id, username, full_name, age=None, date_of_birth=None, state_of_origin=None, gender=None):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.is_active = True
        self.accounts = []
        self.age = age
        self.date_of_birth = date_of_birth
        self.state_of_origin = state_of_origin
        self.gender = gender
