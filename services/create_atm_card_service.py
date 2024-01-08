# services/create_atm_card_service.py
from models.atm_card import ATMCard
from utils.random_generator import generate_random_number

class CreateATMCardService:
    def __init__(self):
        pass

    def execute(self, account):
        # Generate random card details
        card_number = generate_random_number(16)
        pin_number = generate_random_number(4)
        cvc = generate_random_number(3)

        # Create a new ATM card
        atm_card = ATMCard(card_number=card_number, pin_number=pin_number, cvc=cvc, account=account)
        account.atm_card = atm_card

        # Return the created ATM card
        return atm_card
