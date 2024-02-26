class Account:
    def __init__(self, _id: int, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> str or int:
        if amount > self.balance:
            return 'Amount exceeded balance'
        self.balance -= amount
        return self.balance

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
