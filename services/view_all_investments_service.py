# services/view_all_investments_service.py
class ViewAllInvestmentsService:
    def __init__(self):
        pass

    def execute(self, user):
        if user.accounts:
            print(f"All Investments for the User:")

            for account in user.accounts:
                if account.investments:
                    print(f"\nInvestments for Account Number {account.account_id}:")
                    for investment in account.investments:
                        self.print_investment_details(investment)
                else:
                    print(f"No investments for Account Number {account.account_id}.")
        else:
            print("No accounts found for the user.")

    def print_investment_details(self, investment):
        # Print investment details
        print(f"Investment ID: {investment.investment_id}")
        print(f"Amount: ${investment.amount:.2f}")
        print(f"Start Date: {investment.start_date}")
        print(f"Duration (Months): {investment.duration_months}")
        print(f"End Date: {investment.end_date}")

    def print_all_investment_details(self, investments):
        if investments:
            for investment in investments:
                self.print_investment_details(investment)
        else:
            print("No investments found.")
