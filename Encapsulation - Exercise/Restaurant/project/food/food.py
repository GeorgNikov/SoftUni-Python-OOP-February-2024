from project import Product


class Food(Product):

    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        self.__grams = value