# services/make_investments_service.py
from models.investment import Investment
from datetime import datetime

class MakeInvestmentsService:
    def __init__(self):
        pass

    def execute(self, account, amount, duration_months):
        try:
            # Convert the amount and duration to appropriate data types
            amount = float(amount)
            duration_months = int(duration_months)

            # Validate the amount and duration
            if amount <= 0 or duration_months <= 0:
                raise ValueError("Amount and duration must be positive numbers.")

            # Check if the account has sufficient balance
            if amount > account.balance:
                raise ValueError("Insufficient funds for investment.")

            # Deduct the investment amount from the account balance
            account.balance -= amount

            # Generate a unique investment ID (you can use a function to generate one)
            investment_id = self.generate_investment_id()

            # Get the current date and time
            start_date = datetime.now().strftime("%Y-%m-%d")

            # Create a new investment
            investment = Investment(
                investment_id=investment_id,
                account=account,
                amount=amount,
                start_date=start_date,
                duration_months=duration_months
            )

            # Print a success message
            print(f"Investment of ${amount:.2f} successful. Investment ID: {investment_id}")

            # Return the created investment (you might want to use it for further processing)
            return investment

        except ValueError as e:
            # Handle invalid inputs
            print(f"Error: {e}. Unable to process the investment.")

    def generate_investment_id(self):
        # Placeholder for generating a unique investment ID (you can use a more sophisticated method)
        return "INV_" + str(datetime.now().timestamp())
