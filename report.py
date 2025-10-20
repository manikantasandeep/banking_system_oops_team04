"""
report.py — reporting utilities

- account_summary(account): show details + transactions
- bank_summary(bank): total balance, number of accounts
- all_accounts_report(bank): list all accounts in table form
"""

def account_summary(account):
    # TODO: return multi-line string summary
    summary= "account summary\n"
    summary+=f"account id : {account.account_id}\n"
    summary+=f"account name : {account.name}\n"
    summary+=f"account balance :{account.balance}\n"
    if account.history:
        for transaction in account.history:
            summary+=f"{transaction}"
        else:
         summary+="  no transaction is not done yet\n"
        return summary
def bank_summary(bank):
    # TODO: return string with total balance, number of accounts
    total_balance=sum(account.balance for account in bank.accounts.values())
    total_accounts=len(bank.accounts)
    return f"total balance is : {total_balance} and total accounts is : {total_accounts} "
    pass

def all_accounts_report(bank):
    # TODO: return string with all account balances
    for account in bank.accounts.values():
        report=f"account id : {account.account_id} ,name :{account.name}, balance : {account.balance}"
        return report
    pass
# -*- coding: utf-8 -*-

