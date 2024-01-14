# services/create_atm_card_service.py
from models.atm_card import ATMCard
from utils.random_generator import generate_random_number
from datetime import datetime, timedelta

class CreateATMCardService:
    def __init__(self):
        pass

    def execute(self, account, user):
        if account.atm_card:
            print("An ATM card already exists for this account.")
            view_existing_card = input("Do you want to view the existing card details? (yes/no): ").lower()
            if view_existing_card == "yes":
                self.display_card_details(account.atm_card)
            return account.atm_card

        # Use user's full name as card number
        card_number = user.full_name.replace(" ", "").upper()

        # Generate random card details
        pin_number = generate_random_number(4)
        cvc = generate_random_number(3)

        # Generate a random expiration date after the year 2021
        current_year = datetime.now().year
        expiration_year = generate_random_number(current_year + 1, current_year + 10)
        expiration_month = generate_random_number(1, 12)
        expiration_date = datetime(expiration_year, expiration_month, 1) + timedelta(days=29)

        # Create a new ATM card
        atm_card = ATMCard(card_number=card_number, pin_number=pin_number, cvc=cvc, expiration_date=expiration_date, account=account)
        account.atm_card = atm_card

        # Return the created ATM card
        return atm_card

    def display_card_details(self, atm_card):
        print("ATM Card Details:")
        print(f"Card Number: {atm_card.card_number}")
        print(f"PIN: {atm_card.pin_number}")
        print(f"CVC: {atm_card.cvc}")
        print(f"Expiration Date: {atm_card.expiration_date.strftime('%Y-%m')}")
