from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

test = SaltwaterFish("Tomi", "gupa", 2.33)
test2 = FreshwaterFish("Pencho", "heler", 3.12)

aqua = SaltwaterAquarium("Aqua1")
aqua.add_fish(test)
aqua.add_fish(test2)
aqua.add_decoration(Plant())
aqua.add_decoration(Ornament())
print(test.size)
aqua.feed()
print(test.size)

print(aqua)