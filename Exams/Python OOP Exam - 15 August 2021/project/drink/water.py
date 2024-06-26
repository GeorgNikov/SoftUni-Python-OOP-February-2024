from project import Drink


class Water(Drink):
    WATER_PRICE = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.WATER_PRICE, brand)
