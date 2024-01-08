# services/view_recent_transfers_service.py
class ViewRecentTransfersService:
    def __init__(self):
        pass

    def execute(self, account):
        if account.recent_transfers:
            print(f"Recent Transfers for Account Number {account.account_id}:")

            for transfer in account.recent_transfers:
                self.print_transfer_details(transfer)
        else:
            print(f"No recent transfers for Account Number {account.account_id}.")

    def print_transfer_details(self, transfer):
        # Print transfer details
        print(f"Transfer ID: {transfer.transfer_id}")
        print(f"Beneficiary: {transfer.beneficiary_name}")
        print(f"Amount: ${transfer.amount:.2f}")
        print(f"Transfer Date: {transfer.transfer_date}")

    def print_all_transfer_details(self, transfers):
        if transfers:
            for transfer in transfers:
                self.print_transfer_details(transfer)
        else:
            print("No transfers found.")
