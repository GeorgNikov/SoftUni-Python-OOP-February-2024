from project import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_DECREASE = 15
    OXYGEN_UNITS = 90

    def __init__(self, name: str):
        super().__init__(name, oxygen=self.OXYGEN_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE
