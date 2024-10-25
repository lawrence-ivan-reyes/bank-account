from bank_account import BankAccount

# stretch challenge 4
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, full_name, account_type = "checking"):
        new_account = BankAccount(full_name, account_type)
        self.accounts.append(new_account)
        print(f"\nAccount created for {full_name} with account number {new_account.account_number}.")
    