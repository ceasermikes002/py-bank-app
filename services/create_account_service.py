# services/create_account_service.py
from models.account import Account
from models.atm_card import ATMCard
from services.create_atm_card_service import CreateATMCardService
from utils.random_generator import generate_random_number
from datetime import datetime
class CreateAccountService:
    def __init__(self):
        pass

    def execute(self, user):
        try:
            # Collect additional user information
            name = input("Enter your full name: ")
            age = int(input("Enter your age: "))  # Convert age to an integer
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
            atm_card_service = CreateATMCardService()
            atm_card_service.execute(account)

            # Return the created account
            return account
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid numeric age.")
            return None  # You might want to handle this case differently based on your application logic
