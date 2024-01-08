# models/atm_card.py
class ATMCard:
    def __init__(self, card_number, pin_number, cvc, account):
        self.card_number = card_number
        self.pin_number = pin_number
        self.cvc = cvc
        self.account = account  # Reference to the associated account

    def __str__(self):
        return f"ATM Card: {self.card_number}, CVC: {self.cvc}"
