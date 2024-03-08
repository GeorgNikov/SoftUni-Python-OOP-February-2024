from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Cpntroller:
    valid_type_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
    valid_decoration = ["Ornament", "Plant"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @property
    def __get_type_aquariums(self):
        return {"FreshwaterAquarium": FreshwaterAquarium,
                "SaltwaterAquarium": SaltwaterAquarium}

    @property
    def __get_decorations(self):
        return {"Ornament": Ornament,
                "Plant": Plant}

    @property
    def __get_type_fish(self):
        return {"FreshwaterFish": FreshwaterFish,
                "SaltwaterFish": SaltwaterFish}

    def __find_aquarium(self, aquarium_name: str):
        for aqua in self.aquariums:
            if aqua.name == aquarium_name:
                return aqua

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.valid_type_aquariums:
            return "Invalid aquarium type."

        new_aqua = self.__get_type_aquariums[aquarium_type](aquarium_name)
        self.aquariums.append(new_aqua)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.valid_decoration:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration_type)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        pass

