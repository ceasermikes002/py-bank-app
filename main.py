from models.user import User
from services.create_account_service import CreateAccountService
from services.deposit_service import DepositService
from services.withdraw_service import WithdrawService
from services.make_investments_service import MakeInvestmentsService
from services.transfer_service import TransferService
from services.view_recent_transfers_service import ViewRecentTransfersService
from services.create_atm_card_service import CreateATMCardService
from services.view_account_details_service import ViewAccountDetailsService
from services.view_all_investments_service import ViewAllInvestmentsService
from services.delete_account_service import DeleteAccountService
from utils.colors import colorize

def display_menu():
    print("1. Create Account")
    print("2. Deposit")  # You can add deposit service if needed
    print("3. Withdraw")
    print("4. Transfer to Other Beneficiaries")
    print("5. View Recent Transfers")
    print("6. Make Investments")
    print("7. Create ATM Card")
    print("8. View Account Details (including Card Details)")
    print("9. View All Investments")
    print("10. Delete Account")
    print("11. Exit")

def main():
    print(colorize("Welcome to Your Banking App!", "green"))

    user_name = input("What should we call you?: ")
    user = User(user_id=1, username=user_name, full_name=user_name)

    while user.is_active:
        display_menu()

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            create_account_service = CreateAccountService()
            account = create_account_service.execute(user)
            print(colorize(f"Account created successfully!\n"
                            f"Account Number: {account.account_id}\n"
                            f"Name: {account.name}\n"
                            f"Age: {account.age}\n"
                            f"Date of Birth: {account.date_of_birth}\n"
                            f"State of Origin: {account.state_of_origin}\n"
                            f"Gender: {account.gender}\n"
                            f"Account Creation Time: {account.account_creation_time}", "blue"))

        elif choice == "2":  # Include deposit service
            deposit_service = DepositService()
            amount = input("Enter the deposit amount: ")
            deposit_service.execute(user, account, amount)

        elif choice == "3":
            withdraw_service = WithdrawService()
            amount = input("Enter the withdrawal amount: ")
            withdraw_service.execute(account, amount)

        elif choice == "4":  # Include transfer service
            transfer_service = TransferService()
            amount = input("Enter the transfer amount: ")
            beneficiary_name = input("Enter the beneficiary's name: ")
            transfer_service.execute(user, account, amount, beneficiary_name)

        elif choice == "5":  # Include view recent transfers service
            view_recent_transfers_service = ViewRecentTransfersService()
            view_recent_transfers_service.execute(account)

        elif choice == "6":
            make_investments_service = MakeInvestmentsService()
            amount = input("Enter the investment amount: ")
            duration_months = input("Enter the investment duration (in months): ")
            make_investments_service.execute(account, amount, duration_months)

        # Add handling for other menu options here...

        elif choice == "11":
            print(colorize("Thank you for using Your Banking App! Goodbye.", "green"))
            break

        else:
            print(colorize("Invalid choice. Please enter a number between 1 and 11.", "red"))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
