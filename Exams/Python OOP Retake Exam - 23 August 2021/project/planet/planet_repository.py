from project import Planet


class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        planet = [p for p in self.planets if p.name == name]
        return planet[0] if planet else None
