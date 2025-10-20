"""
Account class

Represents a bank account with:
- account_id
- name
- balance
- transaction history
"""

from transaction import Transaction
from exceptions import InsufficientFundsError, InvalidAmountError

class Account:
    def __init__(self, account_id, name, balance=0.0):
        # TODO: initialize attributes, ensure balance >= 0
        self.account_id= account_id
        self.name = name
        self.balance = 0.0
        self.history= []

    def deposit(self, amount, description=""):
        # TODO: validate amount > 0
        # create Transaction("deposit", amount, description)
        # increase balance
        if amount <= 0:
            return InvalidAmountError("Amount must be positive")
        t = Transaction("deposit",amount,description = description)
        self.balance += amount
        self.history.append(t)
        return t

    def withdraw(self, amount, description=""):
        # TODO: ensure balance >= amount
        # create Transaction("withdraw", amount, description)
        # decrease balance
        if self.balance < amount:
            return InsufficientFundsError("Insufficient funds for withdrawal")
        if amount <= 0:
            return InvalidAmountError("Amount must be positive")
        t = Transaction("withdraw",amount,description= description)
        self.balance -= amount
        self.history.append(t)
        return t
        
    def transfer(self, target_account, amount, description=""):
        # TODO: withdraw from self, deposit to target
        # create Transaction("transfer", amount, description)
        if amount <= 0:
            return InvalidAmountError("Amount must be positive")
        if amount > self.balance:
            return InsufficientFundsError("Insufficient funds for transfer")
        t = Transaction("transfer", amount,description="Amount has been transfered")
        self.balance -= amount
        target_account.balance +=amount
        self.history.append(t)

    def get_history(self):
        # TODO: return transaction list
        return self.history

    def __str__(self):
        # TODO: "Account[ID] Name | Balance: Rs.XXX"
        return f"Account[{self.account_id} {self.name} | Balance:Rs.{self.balance}]"
