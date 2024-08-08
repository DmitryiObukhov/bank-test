import unittest
from bank import Bank, SavingsAccount, CurrentAccount, Account


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account1 = SavingsAccount(1, 1000, 3.0)
        self.account2 = CurrentAccount(2, 500, -200)
        self.account3 = Account(3, 1500)

    def test_open_account(self):
        self.bank.open_account(self.account1)
        self.bank.open_account(self.account2)
        self.bank.open_account(self.account3)

        self.assertIn(self.account1, self.bank.accounts)
        self.assertIn(self.account2, self.bank.accounts)
        self.assertIn(self.account3, self.bank.accounts)

    def test_update_accounts(self):
        initial_balance1 = self.account1.balance
        initial_balance2 = self.account2.balance
        initial_balance3 = self.account3.balance

        dividend_amount = 100
        self.bank.pay_dividend(dividend_amount)

        self.bank.update_accounts()

        expected_balance1 = initial_balance1 + (initial_balance1 * (self.account1.interest_rate / 100))
        self.assertAlmostEqual(self.account1.balance, expected_balance1, places=2)

        expected_balance2 = initial_balance2
        self.assertAlmostEqual(self.account2.balance, expected_balance2, places=2)
        self.bank.show_accounts()

        expected_balance3 = initial_balance3
        self.assertAlmostEqual(self.account3.balance, expected_balance3, places=2)


if __name__ == '__main__':
    unittest.main()
