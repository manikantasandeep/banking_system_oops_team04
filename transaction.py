# -*- coding: utf-8 -*-

"""
Transaction class

Represents a single transaction: type, amount, timestamp, description.
"""

from utils import current_timestamp
from exceptions import InvalidAmountError
class Transaction:
    def __init__(self, tx_type, amount, description="", timestamp=None):
        """
        tx_type: "deposit", "withdraw", "transfer"
        amount: positive float
        description: text about transaction
        timestamp: auto-generate if None
        """
        # TODO: validate amount > 0
        # if timestamp is None: use current_timestamp()
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.tx_type = tx_type
        self.amount = amount  
        self.description = description
        self.timestamp = current_timestamp() if timestamp is None else timestamp
    def as_dict(self):
        # TODO: return dict representation
        return {
            "type":self.tx_type,
            "amount":self.amount,
            "description":self.description,
            "timestamp":self.timestamp
            }

    def __str__(self):
        # TODO: "[TIMESTAMP] TYPE: AMOUNT — description"
        return f"[{self.timestamp}] TYPE: {self.amount} - {self.description}"
