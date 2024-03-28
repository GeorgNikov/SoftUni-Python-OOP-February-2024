from project import ElbowPad
from project import KneePad
from project import IndoorTeam
from project import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAMS = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT[equipment_type]()

        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return f"Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._get_equipment(equipment_type)
        team = self._get_team(team_name)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for equip in self.equipment:
            if equip.__class__.__name__ == equipment_type:
                equip.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team(team_name1)
        team2 = self._get_team(team_name2)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_protection = sum(p.price for p in team1.equipment)
        team2_protection = sum(p.price for p in team2.equipment)

        points_of_team1 = team1.advantage + team1_protection
        points_of_team2 = team2.advantage + team2_protection

        if points_of_team1 > points_of_team2:
            team1.win()
            return f"The winner is {team1.name}."
        if points_of_team2 > points_of_team1:
            team2.win()
            return f"The winner is {team2.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:"]
        [result.append(t.get_statistics()) for t in sorted_teams]

        return "\n".join(result)

    def _get_equipment(self, equipment_type: str):
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        return equipment[-1] if equipment else None

    def _get_team(self, team_name: str):
        team = [t for t in self.teams if t.name == team_name]
        return team[0] if team else None
