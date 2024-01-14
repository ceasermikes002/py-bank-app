# services/deposit_service.py
class DepositService:
    def __init__(self):
        pass

    def authenticate_user(self, user, account):
        try:
            # Check if the account has an associated ATM card
            if account.atm_card is None:
                raise ValueError("No ATM card associated with the account. Please create a card first.")

            # Authenticate the user based on the card's PIN
            pin_input = input("Enter your ATM card PIN: ")
            if pin_input == account.atm_card.pin_number:
                return True
            else:
                print("Authentication failed. Incorrect PIN.")
                return False
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def execute(self, user, account):
        try:
            # Authenticate the user based on the card's PIN
            if not self.authenticate_user(user, account):
                return

            # User authenticated
            # Move the amount input inside the authenticated block
            amount = float(input("Enter the deposit amount: "))

            # Ensure the amount is greater than 100 naira
            if amount <= 100:
                raise ValueError("Initial deposit amount must be greater than 100 naira.")

            # Update the account balance
            account.balance += amount

            # Print a success message
            print(f"Congratulations, {user.full_name}! Initial deposit of ₦{amount:.2f} successful. New balance: ₦{account.balance:.2f}")
        except ValueError as e:
            # Handle invalid amount input
            print(f"Error: {e}. Please enter a valid initial deposit amount greater than 100 naira.")
