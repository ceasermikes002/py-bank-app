# services/deposit_service.py
class DepositService:
    def __init__(self):
        pass

    def execute(self, user, account, amount):
        try:
            # Authenticate the user based on name and account number
            user_name_input = input("Enter your full name: ")
            account_number_input = input("Enter your account number: ")

            if user_name_input == user.full_name and account_number_input == account.account_id:
                # User authenticated
                # Convert the amount to a float
                amount = float(amount)

                # Ensure the amount is greater than 100 naira
                if amount <= 100:
                    raise ValueError("Initial deposit amount must be greater than 100 naira.")

                # Update the account balance
                account.balance += amount

                # Print a success message
                print(f"Congratulations, {user.full_name}! Initial deposit of ₦{amount:.2f} successful. New balance: ₦{account.balance:.2f}")
            else:
                print("Authentication failed. Please ensure your name and account number match.")
        except ValueError as e:
            # Handle invalid amount input
            print(f"Error: {e}. Please enter a valid initial deposit amount greater than 100 naira.")
