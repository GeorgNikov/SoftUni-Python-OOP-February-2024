from project import Geodesist
from project import Biologist
from project import Meteorologist
from project import Planet
from project import PlanetRepository
from project import AstronautRepository


class SpaceStation:
    ASTRONAUT_TYPE = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in self.ASTRONAUT_TYPE:
            raise Exception("Astronaut type is not valid!")

        new_astronaut = self.ASTRONAUT_TYPE[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(', ')
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        astronauts_deque = sorted(suitable_astronauts, key=lambda a: a.oxygen, reverse=True)[:5]
        if not astronauts_deque:
            raise Exception(f"You need at least one astronaut to explore the planet!")

        # collect items
        participated_astronauts = 0

        for astronaut in astronauts_deque:
            if not planet.items:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if not planet.items:
            self.number_of_successful_missions += 1
            return (f"Planet: {planet_name} was explored. {participated_astronauts} "
                    f"astronauts participated in collecting items.")

        self.number_of_not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.number_of_successful_missions} successful missions!\n" \
                 f"{self.number_of_not_completed_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + '\n'

        return result.strip()
