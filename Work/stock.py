class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, count_shares: int):
        self.shares -= count_shares


class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()

    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
        self.__super__ = super()
