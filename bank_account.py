import random

class BankAccount:
    def __init__(self, full_name, account_type="checking"): # stretch challenge 1: initializing account type to checking at first
        # attributes for the BankAccount class
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999) # randomly generated 8 digit number, unique per account
        self.balance = 0
        self.account_type = account_type.lower() # stretch challenge 1: converting to lowercase for case insensitivity (just in case)

    # class methods
    def deposit(self, amount):
        self.balance += amount 
        print(f"Amount Deposited: ${amount:.2f} > New Balance: ${self.balance:.2f}") # .2f across the entire project to have 2 decimal places across all dollar values in the output

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds. You have also been charged an overdraft fee of $10.00.\nYour new balance is: ${self.balance:.2f}")
        else: 
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.2f} > New Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Hi, {self.full_name}! Your current account balance is ${self.balance:.2f}.")
        return self.balance
    
    def add_interest(self):
        if self.account_type == "savings":
            interest = round(self.balance * 0.01, 2) # stretch challenge 1: savings interest of 1% monthly
        else:
            interest = round(self.balance * 0.00083, 2) # stretch challenge 1: original interest rate (now for checkings)
        
        self.balance += interest
        print(f"You have gained an interest of ${interest}, bringing your total current balance to: ${self.balance:.2f}.") 

    def print_statement(self):
        masked_account_number = "****" + str(self.account_number)[4:]
        print(f"Account Details:\n{self.full_name}\nAccount No.: {masked_account_number}\nBalance: ${self.balance:.2f}")

# 3 different bank accounts
user_harry = BankAccount("Harry Potter")
user_harry.deposit(100)
user_harry.withdraw(50)
user_harry.get_balance()
user_harry.add_interest()
print("\n")
user_harry.print_statement()
print("\n---\n")

user_ron = BankAccount("Ron Weasley")
user_ron.deposit(150)
user_ron.withdraw(200)
user_ron.get_balance()
user_ron.add_interest()
print("\n")
user_ron.print_statement()
print("\n---\n")

user_hermione = BankAccount("Hermione Granger")
user_hermione.deposit(200)
user_hermione.withdraw(100)
user_hermione.get_balance()
user_hermione.add_interest()
print("\n")
user_hermione.print_statement()
print("\n---\n")

# creating a checking account and a savings account for user Mitchell for stretch challenge 1
user_mitchell_checking = BankAccount("Mitchell", "checking")
user_mitchell_savings = BankAccount("Mitchell", "savings")

# deposit $400,000 into both accounts
user_mitchell_checking.deposit(400000)
user_mitchell_savings.deposit(400000)
user_mitchell_checking.print_statement()
print("\n")
user_mitchell_savings.print_statement()
print("\n---\n")

# add interest to each account and print statements
user_mitchell_checking.add_interest()
user_mitchell_checking.print_statement()
print("\n")

user_mitchell_savings.add_interest()
user_mitchell_savings.print_statement()