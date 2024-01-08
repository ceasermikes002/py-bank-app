# models/account.py
class Account:
    def __init__(self, account_id, user, name, age, date_of_birth, state_of_origin, gender, account_creation_time, balance=0):
        self.account_id = account_id
        self.user = user
        self.name = name
        self.age = age
        self.date_of_birth = date_of_birth
        self.state_of_origin = state_of_origin
        self.gender = gender
        self.account_creation_time = account_creation_time
        self.balance = balance
        self.atm_card = None
        self.investments = []
        self.recent_transfers = []
