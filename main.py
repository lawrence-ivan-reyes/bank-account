# moving all code outside of BankAccount & Bank classes to this main file for organization

from bank_account import BankAccount

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

# stretch challenge 1: creating a checking account and a savings account Mitchell
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
print("\n---\n")

# stretch challenge 2
bank = [user_harry, user_ron, user_hermione, user_mitchell_checking, user_mitchell_savings]

def interest_all(accounts):
    for account in accounts:
        account.add_interest()

interest_all(bank) 
print("\n---\n")

for account in bank:
    account.print_statement()
    print("\n---\n")

# stretch challenge 3
while True:
    option = input("Welcome to the Dominican Bank! Please choose an option:\n(1) Create Account\n(2) Check Statement\n(3) Deposit\n(4) Withdraw\n(5) Exit\n> ")

    if option == '1':
        name = input("\nEnter full name: ")

        while True:
            account_type_input = input("Enter account type (1 for checking, 2 for savings): ").strip()
            if account_type_input == '1':
                account_type = "checking"
                break
            elif account_type_input == '2':
                account_type = "savings"
                break
            else:
                print("\nInvalid input for account type. Please enter 1 for checking or 2 for savings.") 

        new_account = BankAccount(name, account_type)
        bank.append(new_account)
        print(f"\nSuccess! Account created for {name} with account number {new_account.account_number}.\n")
    
    elif option == '2':
        account_number = int(input("\nEnter account number to check statement: "))
        account_found = False
        for account in bank:
            if account.account_number == account_number:
                account.print_statement()
                account_found = True
                break
        if not account_found:
            print("\nAccount number not found.")

    elif option == '3':
        account_number = int(input("\nEnter account number to deposit: "))
        amount = float(input("Enter amount to deposit: "))
        account_found = False
        for account in bank:
            if account.account_number == account_number:
                account.deposit(amount)
                account_found = True
                break
        if not account_found:
            print("\nAccount number not found.")

    elif option == '4':
        account_number = int(input("\nEnter account number to withdraw: "))
        amount = float(input("Enter amount to withdraw: "))
        account_found = False
        for account in bank:
            if account.account_number == account_number:
                account.withdraw(amount)
                account_found = True
                break
        if not account_found:
            print("\nAccount number not found.")

    elif option == '5':
        print("\nThank you for using Dominican Bank. See you next time!")
        break

    else:
        print("\nInvalid. Please choose a valid option.")