from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_DECREASE = 5
    OXYGEN_UNITS = 70

    def __init__(self, name: str):
        super().__init__(name, oxygen=self.OXYGEN_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE
