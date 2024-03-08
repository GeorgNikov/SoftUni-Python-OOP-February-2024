from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    FISH_SIZE = 3
    AFTER_EAT = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.FISH_SIZE, price)

    def eat(self):
        self.size += self.AFTER_EAT
