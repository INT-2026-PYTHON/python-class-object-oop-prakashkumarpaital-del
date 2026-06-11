"""
## 2. Bank Account Class  *(Medium)*

=================================================
BANK ACCOUNT CLASS
=================================================

Problem Statement:
Write a Python CLASS called `BankAccount`
that represents a simple bank account. Each
account has an account holder's name, a
unique account number, and a balance that
starts at 0 unless an opening balance is
given.

The class must support deposits, withdrawals,
and balance checks. Reject invalid operations
(negative amounts, overdrafts) by printing a
clear message — do NOT crash.

-------------------------------------------------
Instructions:
1. Define a class:
      class BankAccount:
2. Constructor:
      def __init__(self, name, account_number,
                   opening_balance=0):
          - validate that opening_balance >= 0
          - store name, account_number, balance
            on `self`
3. Instance methods:
      - deposit(self, amount)
            * reject amount <= 0 with a message
            * otherwise add to balance
      - withdraw(self, amount)
            * reject amount <= 0
            * reject if amount > balance
            * otherwise subtract from balance
      - get_balance(self)
            * return the current balance
      - __str__(self)
            * return a friendly string like:
              "Account[001 - Alice]: $500"
4. In the driver code:
      - create AT LEAST TWO accounts
      - perform some valid deposits / withdraws
      - perform AT LEAST ONE invalid operation
        (negative amount or overdraft) on each
        account to show the rejection message
      - print each account using print(acc),
        which triggers __str__
5. Do NOT use:
   - class-level mutable defaults (e.g. a list
     as default argument)
   - global variables

-------------------------------------------------
Input Example:
a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob",   "002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)   # overdraft -> rejected
a2.deposit(-50)     # invalid   -> rejected
a2.deposit(300)

Output Example:
Insufficient funds for Alice (balance=600, asked=2000)
Deposit amount must be > 0 (got -50)
Account[001 - Alice]: $600
Account[002 - Bob]:   $300

-------------------------------------------------
Explanation:
- `self.balance` is independent for every
  object, so Alice and Bob keep separate
  balances.
- Validation in `deposit` and `withdraw` shows
  how methods use `self` to read AND update
  state on the same object.
- `__str__` returns the human-readable form
  used by print().
=================================================

"""
class BankAccount:
    def __init__(self, name, account_number, opening_balance=0):
        if opening_balance < 0:
            print(f"Warning: Opening balance cannot be negative. Setting balance to 0 for {name}'s account.")
            self.balance = 0
        else:
            self.balance = opening_balance
        self.name = name
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit amount must be > 0 (got {amount})")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal amount must be > 0 (got {amount})")
        elif amount > self.balance:
            print(f"Insufficient funds for {self.name} (balance={self.balance}, asked={amount})")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number} - {self.name}]: ${self.balance}"


def get_numeric_input(prompt, default_value=None):
    while True:
        user_input = input(prompt)
        if not user_input and default_value is not None:
            return default_value
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("\n--- Enter Details for Account 1 ---")
name1 = input("Enter account holder's name: ")
acc_num1 = input("Enter account number: ")
opening_balance1 = get_numeric_input("Enter opening balance (press Enter for 0): ", 0)
a1 = BankAccount(name1, acc_num1, opening_balance1)

print("\n--- Enter Details for Account 2 ---")
name2 = input("Enter account holder's name: ")
acc_num2 = input("Enter account number: ")
opening_balance2 = get_numeric_input("Enter opening balance (press Enter for 0): ", 0)
a2 = BankAccount(name2, acc_num2, opening_balance2)

print(f"\n--- Performing Operations on {a1.name}'s Account ---")
deposit_amount1 = get_numeric_input("Enter deposit amount for account 1: ")
a1.deposit(deposit_amount1)

withdraw_amount1 = get_numeric_input("Enter withdrawal amount for account 1: ")
a1.withdraw(withdraw_amount1)

invalid_withdraw1 = get_numeric_input("Enter an invalid withdrawal amount for account 1: ")
a1.withdraw(invalid_withdraw1)

print(f"\n--- Performing Operations on {a2.name}'s Account ---")
deposit_amount2 = get_numeric_input("Enter deposit amount for account 2: ")
a2.deposit(deposit_amount2)

invalid_deposit2 = get_numeric_input("Enter an invalid deposit amount for account 2: ")
a2.deposit(invalid_deposit2)

print("\n--- Final Account States ---")
print(a1)
print(a2)