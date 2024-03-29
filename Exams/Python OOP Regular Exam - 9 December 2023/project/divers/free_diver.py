from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN = 120
    OXYGEN_DECREASE = 0.6

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.DEFAULT_OXYGEN)

    def miss(self, time_to_catch: int):
        oxygen = round(time_to_catch * FreeDiver.OXYGEN_DECREASE)
        reduce_oxygen = self.oxygen_level - oxygen
        self.oxygen_level = max(reduce_oxygen, 0)

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.DEFAULT_OXYGEN
