# services/transaction_service.py
from models.account import Account
from models.atm_card import ATMCard
from models.investment import Investment
from utils.random_generator import generate_random_number
from datetime import datetime

class TransactionService:
    
    def create_account(self, user):
        # Collect additional user information
        name = input("Enter your full name: ")
        age = input("Enter your age: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        state_of_origin = input("Enter your state of origin: ")
        gender = input("Enter your gender: ")

        # Generate a random 10-digit account number
        account_number = generate_random_number(10)

        # Get the current date and time
        account_creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a new account
        account = Account(
            account_id=account_number,
            user=user,
            name=name,
            age=age,
            date_of_birth=dob,
            state_of_origin=state_of_origin,
            gender=gender,
            account_creation_time=account_creation_time
        )
        user.accounts.append(account)

        # Create an ATM card for the account
        atm_card = self.create_atm_card(account)
        account.atm_card = atm_card

        # Return the created account
        return account

    def create_atm_card(self, account):
        # Generate random card details
        card_number = generate_random_number(16)
        pin_number = generate_random_number(4)
        cvc = generate_random_number(3)

        # Create a new ATM card
        atm_card = ATMCard(card_number=card_number, pin_number=pin_number, cvc=cvc, account=account)
        account.atm_card = atm_card

        # Return the created ATM card
        return atm_card

    # Other methods (deposit, withdraw, transfer, etc.) will be added here

    # ...
