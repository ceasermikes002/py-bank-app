# services/transfer_service.py
import datetime


class TransferService:
    def __init__(self):
        self.transfer_history = []

    def execute(self, account, beneficiary_name, amount):
        try:
            # Convert the amount to a float
            amount = float(amount)

            # Validate the amount
            if amount <= 0:
                raise ValueError("Amount must be a positive number for the transfer.")

            # Check if the account has sufficient balance
            if amount > account.balance:
                raise ValueError("Insufficient funds for the transfer.")

            # Deduct the transfer amount from the account balance
            account.balance -= amount

            # Store the transfer details in the transfer history
            transfer_details = {
                "beneficiary_name": beneficiary_name,
                "amount": amount,
                "timestamp": self.get_current_timestamp()
            }
            self.transfer_history.append(transfer_details)

            # Print a success message
            print(f"Transfer of ${amount:.2f} to {beneficiary_name} successful.")

        except ValueError as e:
            # Handle invalid inputs
            print(f"Error: {e}. Unable to process the transfer.")

    def get_current_timestamp(self):
        # Placeholder for getting the current timestamp (you can use a more sophisticated method)
        return str(datetime.now())
