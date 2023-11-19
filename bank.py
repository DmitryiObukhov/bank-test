class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < 0:
            print(f"Overdraft letter sent for Account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed.")

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts:
            print(account)


account1 = SavingsAccount(1, 1000, 3.0)
account2 = CurrentAccount(2, 500, -200)
account3 = Account(3, 1500)

bank = Bank()
bank.open_account(account1)
bank.open_account(account2)
bank.open_account(account3)

bank.show_accounts()

bank.pay_dividend(100)
bank.update_accounts()

bank.show_accounts()
