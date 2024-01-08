# services/delete_account_service.py
class DeleteAccountService:
    def __init__(self):
        pass

    def execute(self, user):
        # Display a warning and confirmation message
        confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()

        if confirmation == "yes":
            # Deactivate the user account
            user.is_active = False
            print("Your account has been deleted. Thank you for using our services.")
        else:
            print("Account deletion canceled. Your account remains active.")

        # No need to return anything for this example
