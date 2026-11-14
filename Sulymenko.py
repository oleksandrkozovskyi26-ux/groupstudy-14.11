from Kravchenko import Bicycle

class Client:
    def __init__(self, name: str, balance: float, current_bicycle: Bicycle = None):
        self.name = name
        self.balance = balance
        self.current_bicycle = current_bicycle

    def set_bicycle(self, bicycle: Bicycle):
        if self.current_bicycle is not None:
            return False

        self.current_bicycle = bicycle
        return True

    def return_bicycle(self):
        if self.current_bicycle is None:
            return None

        bicycle = self.current_bicycle
        self.current_bicycle = None
        return bicycle

    def deduct_money(self, amount: float):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True
