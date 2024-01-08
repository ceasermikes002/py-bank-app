# services/withdraw_service.py
class WithdrawService:
    def __init__(self):
        pass

    def execute(self, account, amount):
        try:
            # Convert the amount to a float
            amount = float(amount)

            # Validate the amount
            if amount <= 0:
                raise ValueError("Withdrawal amount must be a positive number.")

            # Check if the account has sufficient balance
            if amount > account.balance:
                raise ValueError("Insufficient funds for withdrawal.")

            # Deduct the withdrawal amount from the account balance
            account.balance -= amount

            # Print a success message
            print(f"Withdrawal of ${amount:.2f} successful. New balance: ${account.balance:.2f}")

        except ValueError as e:
            # Handle invalid amount input
            print(f"Error: {e}. Please enter a valid positive number for the withdrawal.")
