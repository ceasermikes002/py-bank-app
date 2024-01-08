# models/investment.py
from datetime import datetime, timedelta

class Investment:
    def __init__(self, investment_id, account, amount, start_date, duration_months):
        self.investment_id = investment_id
        self.account = account  # Reference to the associated account
        self.amount = amount
        self.start_date = start_date
        self.duration_months = duration_months
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self):
        # Convert the start_date string to a datetime object
        start_datetime = datetime.strptime(self.start_date, "%Y-%m-%d")

        # Calculate the end date by adding the duration in months to the start date
        end_datetime = start_datetime + timedelta(days=30 * self.duration_months)

        # Format the end date as a string in the same format as start_date
        end_date_str = end_datetime.strftime("%Y-%m-%d")

        return end_date_str

    def __str__(self):
        return f"Investment ID: {self.investment_id}, Amount: {self.amount}, Duration: {self.duration_months} months, End Date: {self.end_date}"
