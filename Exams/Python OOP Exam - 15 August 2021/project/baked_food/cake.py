from project import BakedFood


class Cake(BakedFood):
    PORTION_SIZE = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION_SIZE, price)
