# Banking System — Student Project

## Project Structure:

banking_system
│── main.py               # Entry point (menu-driven)
│── account.py            # Account class
│── transaction.py        # Transaction class
│── bank.py               # Bank management class
│── report.py             # Reporting utilities
│── exceptions.py         # Custom exception
│── utils.py              # Helper functions (id generation, timestamp)
│── data/
│   └── sample\_data.json  # Optional starter dataset
│── README.md


## Problem Statement
Develop a banking system that supports account creation, deposits, withdrawals, and transfers.  
The system should validate balance availability and throw errors when needed.

## Topics Covered
- Classes: Account, Transaction, Bank\
- OOP methods: deposit, withdraw, transfer
- Custom exceptions for overdrafts and invalid inputs
- File I/O (optional JSON export)
- Modular design with multiple files

## Suggested Team Split
- Student A: `transaction.py` + `account.py`
- Student B: `bank.py` + `exceptions.py`
- Student C: `report.py` + `main.py` + `utils.py`

## Sequence Flow
- `main.py` → imports `Bank`, `Account`, `Report`, `utils`.
- `Bank` → imports `Account`, `exceptions`.
- `Account` → imports `Transaction`.
- `Transaction` → uses `utils.current\_timestamp()`.
- `Report` → imports `Bank` and `Account`.

## Steps
1. Implement `Transaction` → log every deposit/withdraw/transfer.
2. Implement `Account` → holds balance, methods for transactions.
3. Implement `Bank` → manages accounts.
4. Implement `Report` → generate summaries.
5. Implement CLI in `main.py`.



