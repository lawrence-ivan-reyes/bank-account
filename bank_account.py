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
        print(f"Amount Deposited: ${amount} > New Balance: ${self.balance}")

    def withdraw(self, amount):
        amount += self.balance
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds. You have also been charged an overdraft fee of $10.\nYour new balance is: ${self.balance}")
        else: 
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount} > New Balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current account balance is ${self.balance}.")
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"You have gained an interest of ${interest}, bringing your total current balance to: ${self.balance}")

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: {self.account_number}\nBalance: {self.balance}") # figure out a way to hide the first 4 account numbers

# 3 different bank accounts

user_harry = BankAccount("Harry Potter")
user_harry.deposit(100)
user_harry.withdraw(50)

user_ron = BankAccount("Ron Weasley")
user_ron.deposit(150)
user_ron.withdraw(200)

user_hermione = BankAccount("Hermione Granger")
user_hermione.deposit(200)
user_hermione.withdraw(100)