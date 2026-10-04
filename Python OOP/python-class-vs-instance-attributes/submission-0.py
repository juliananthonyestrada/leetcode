class BankAccount: 
    total_balance = 0
    total_accounts = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance # might need to be private
        BankAccount.total_balance += balance
        BankAccount.total_accounts += 1



alice = BankAccount(name="Alice", balance=1000)
bob = BankAccount(name="Bob", balance=2000)

print(f"Alice's balance: ${alice.balance}")
print(f"Bob's balance: ${bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
