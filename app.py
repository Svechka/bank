class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount. Please enter a positive number."
        self.balance += amount
        return f"Deposited {amount} units. New balance: {self.balance} units."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive number."
        if amount > self.balance:
            return "Insufficient funds. Withdrawal not allowed."
        self.balance -= amount
        return f"Withdrew {amount} units. New balance: {self.balance} units."

    def get_balance(self):
        return f"Account balance for {self.account_holder}: {self.balance} units."


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if account_number in self.accounts:
            return "Account already exists with this account number."
        new_account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = new_account
        return f"Account created successfully for {account_holder}."

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return "Account not found. Please check the account number."

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            return "Invalid account number(s) provided."
        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]
        if amount <= 0:
            return "Invalid transfer amount. Please enter a positive number."
        if amount > from_account.balance:
            return "Insufficient funds. Transfer not allowed."
        from_account.balance -= amount
        to_account.balance += amount
        return f"Transferred {amount} units from {from_account.account_holder} to {to_account.account_holder}."

    def get_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts.values())
        return f"Total balance in the bank: {total_balance} units."


# Example Usage:
if __name__ == "__main__":
    bank = Bank()

    print(bank.create_account("123456789", "John Doe", 1000))
    print(bank.create_account("987654321", "Jane Smith", 500))

    account1 = bank.get_account("123456789")
    account2 = bank.get_account("987654321")

    print(account1.get_balance())
    print(account2.get_balance())

    print(account1.deposit(500))
    print(account2.withdraw(200))

    print(account1.get_balance())
    print(account2.get_balance())

    print(bank.transfer("123456789", "987654321", 300))

    print(account1.get_balance())
    print(account2.get_balance())

    print(bank.get_total_balance())
