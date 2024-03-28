from project import BaseTeam


class IndoorTeam(BaseTeam):
    TYPE_ = "IndoorTeam"
    @property
    def get_budget(self):
        return 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.get_budget)

    def win(self):
        self.advantage += 145
        self.wins += 1
