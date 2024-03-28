from project import BaseTeam


class OutdoorTeam(BaseTeam):
    TYPE_ = "OutdoorTeam"
    @property
    def get_budget(self):
        return 1_000.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.get_budget)

    def win(self):
        self.advantage += 115
        self.wins += 1