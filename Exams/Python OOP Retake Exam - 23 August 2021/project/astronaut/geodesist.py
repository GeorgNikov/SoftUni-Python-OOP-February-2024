from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN_DECREASE = 10
    OXYGEN_UNITS = 50

    def __init__(self, name: str):
        super().__init__(name, oxygen=self.OXYGEN_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE
