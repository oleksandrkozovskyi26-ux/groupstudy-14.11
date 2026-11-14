class Client:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def deduct_money(self, amount: float):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True
