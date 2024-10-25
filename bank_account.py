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
        interest = round(self.balance * 0.00083, 2) # added rounding to bring this number to 2 decimal places
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

# requirement #6 from the assignmemt instructions
user_mitchell = BankAccount("Mitchell")
user_mitchell.deposit(400000)
user_mitchell.print_statement()
print("\n")

user_mitchell.add_interest()
user_mitchell.print_statement()  
print("\n")

user_mitchell.withdraw(150)
user_mitchell.print_statement() 