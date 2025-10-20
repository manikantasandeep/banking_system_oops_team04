"""
Bank class

Manages multiple accounts in a dictionary.
"""

from account import Account
from exceptions import AccountNotFoundError
from utils import generate_account_id

class Bank:
    def __init__(self):
        self.accounts = {}
        
        
    def create_account(self, name, initial_balance=0.0):
        # TODO: generate id, create Account, store in dict
        account_id = generate_account_id()
        if account_id in self.accounts:
            account_id = generate_account_id()
        self.accounts[account_id]  = Account(account_id, name)
        return self.accounts[account_id]
    def get_account(self, account_id):
        # TODO: return account or raise AccountNotFoundError
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account not found")
        return self.accounts[account_id]

    def transfer_between_accounts(self, from_id, to_id, amount):
        # TODO: fetch accounts, call transfer()
        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)
        return from_acc.transfer(to_acc,amount,description="Amount transfer")

    def total_balance(self):
        # TODO: sum all balances
        return sum(a.balance for a in self.accounts.values())

    def list_accounts(self):
        # TODO: return list of accounts
        return list(self.accounts.values())
