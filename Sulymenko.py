class Client:
    def __init__(self, name: str, balance: float, bike=None):
        self.name = name
        self.balance = balance
        self.bike = bike

    def deduct_money(self, amount: float):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True
