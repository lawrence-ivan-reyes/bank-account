# Bank Account 🏦
### Ivan Reyes | ACS 1111: Object Oriented Programming | Dani Roxberry 

---

### ℹ️ Program Description
Bank Account is a text-based Python program that simulates a bank—using object oriented programming. Key features of this program:
- Create bank accounts with unique 8-digit account numbers. 
- Perform deposits and withdrawals with real-time balance updates.
- Get an interest on account balance monthly based on account type (checking or savings).
- Print statements showing masked account number, owner’s name, and current balance.
- Interact CLI to manage multiple accounts and perform transactions

---

### ❗️ How To Use
1. **Clone the Repository**  
**HTTPS:** `git clone https://github.com/lawrence-ivan-reyes/bank-account.git`  
**SSH:** `git clone git@github.com:lawrence-ivan-reyes/bank-account.git`  
**GitHub CLI:** `gh repo clone lawrence-ivan-reyes/bank-account`  

2. **Run the Program**  
Run the `main.py` file to start interacting with the banking application.  
`python3 main.py`

3. **Program Features**  
- **Create Account:** Add new bank accounts, specifying owner’s name and account type.
- **Check Statement:** View a bank statement for any account.
- **Deposit Funds:** Deposit a specific amount into an account.
- **Withdraw Funds:** Withdraw a specific amount, with overdraft fees if balance is insufficient.
- **Exit:** End the session.

4. **Example Commands**   
After starting the program, use the options provided in the menu to create accounts, deposit or withdraw funds, and check statements.

5. **Interest Calculation**  
Each month, the balance accrues interest:
- **Checking Account:** 0.083% interest per month.
- **Savings Account:** 1% interest per month.

---

### 💻 Code Structure
- `bank_account.py`: Contains the `BankAccount` class, with methods for deposits, withdrawals, balance inquiry, interest calculation, and statement printing.
- `main.py`: Manages account creation, transactions, and interaction with the user.

---

### 🌐 Example Output
Here is an example account interaction output:

`Welcome to the Royal Bank of Dominican!`  
`Please choose an option:`  
`(1) Create Account`  
`(2) Check Statement`  
`(3) Deposit`  
`(4) Withdraw`  
`(5) Exit`  

---

### 📘 Resources
For string formatting, specifically with modifiers that allows this program to output values of a maximum of 2 decimal places, check out the following resource on Python string formatting:
- [Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp)