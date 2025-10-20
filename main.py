"""
CLI for banking system

Menu:
1. Create account
2. Deposit
3. Withdraw
4. Transfer
5. Account summary
6. Bank summary
0. Exit
"""
from bank import Bank
from report import account_summary, bank_summary, all_accounts_report

def main():
  
    # TODO: create Bank instance
    # loop menu and call methods
    # handle exceptions with try/except
    bank=Bank()
    while True:
        print("Menu :")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Account summary")
        print("6. Bank summary")
        print("0. Exit")
        choice=input("enter your choice :")
        try:
            if choice=='1':
                name=input("enter your name :")
                account = bank.create_account(name)
                print(f"account id : {account.account_id} and account name : {account.name}")
            elif choice == '2':
                account_id = input("enter account id: ")
                amount = float(input("enter deposit amount: "))
                description = input("enter description: ")
                account= bank.get_account(account_id)
                account.deposit(amount, description)
                print("deposit successful.")
            elif choice == '3':
                account_id = input("enter account id: ")
                amount = float(input("enter amount: "))
                account = bank.get_account(account_id)
                account.withdraw(amount)
                print("withdraw successful.")
            elif choice == '4':
                from_id = input("from account id: ")
                to_id = input("to account id: ")
                amount = float(input("enter your transfer amount: "))
                bank.transfer_between_accounts(from_id, to_id, amount)
                print("transfer successful.")
            elif choice == '5':
                account_id = input("enter account id: ")
                account = bank.get_account(account_id)
                print(account_summary(account))
            elif choice == '6':
                print(bank_summary(bank))
                print(all_accounts_report(bank))
            elif choice == '0':
                print("exit thankyou")
                break
            else:
                print("invalid choice")
        except Exception as e:
            print("error:", e)
    pass
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-

