from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    DEFAULT_OXYGEN = 540
    OXYGEN_DECREASE = 0.3

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.DEFAULT_OXYGEN)

    def miss(self, time_to_catch: int):
        oxygen = round(time_to_catch * ScubaDiver.OXYGEN_DECREASE)
        reduce_oxygen = self.oxygen_level - oxygen
        self.oxygen_level = max(reduce_oxygen, 0)

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.DEFAULT_OXYGEN