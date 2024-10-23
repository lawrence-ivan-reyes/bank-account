import random

class BankAccount:
    def __init__(self, full_name):
        # attributes for the BankAccount class
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999) # randomly generated 8 digit number, unique per account
        self.balance = 0

    # class methods
    def deposit(self, amount):
        self.balance += amount 
        print(f"Amount Deposited: ${amount} New Balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print("Insufficient funds. You have also been charged an overdraft fee of $10.")
            self.balance -= 10
        else: 
            print(f"Amount Withdrawn: ${amount} New Balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current account balance is: ${self.balance}")
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"You have gained an interest of ${interest}, bringing your total current balance to: ${self.balance}")

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: {self.account_number}\nBalance: {self.balance}") # figure out a way to hide the first 4 account numbers

