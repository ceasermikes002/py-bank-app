# services/view_account_details_service.py
class ViewAccountDetailsService:
    def __init__(self):
        pass

    def execute(self, account):
        # Print account details
        print(f"Account Details for Account Number {account.account_id}:")
        print(f"Name: {account.name}")
        print(f"Age: {account.age}")
        print(f"Date of Birth: {account.date_of_birth}")
        print(f"State of Origin: {account.state_of_origin}")
        print(f"Gender: {account.gender}")
        print(f"Account Creation Time: {account.account_creation_time}")
        print(f"Account Balance: ${account.balance:.2f}")

        # Check if the account has an ATM card
        if account.atm_card:
            self.print_card_details(account.atm_card)
        else:
            print("No ATM Card associated with this account.")

    def print_card_details(self, atm_card):
        # Print ATM card details
        print("\nATM Card Details:")
        print(f"Card Number: {atm_card.card_number}")
        print(f"PIN: {atm_card.pin_number}")
        print(f"CVC: {atm_card.cvc}")
