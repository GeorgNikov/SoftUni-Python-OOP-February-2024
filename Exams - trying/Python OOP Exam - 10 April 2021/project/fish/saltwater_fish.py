from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    FISH_SIZE = 5
    AFTER_EAT = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.FISH_SIZE, price)

    def eat(self):
        self.size += self.AFTER_EAT
