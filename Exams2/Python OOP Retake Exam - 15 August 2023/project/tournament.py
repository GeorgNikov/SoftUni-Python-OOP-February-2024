from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAM = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

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
        if team_type not in self.VALID_TEAM:
            raise Exception("Invalid team type!")

        if self.capacity == len(self.teams):
            return f"Not enough tournament capacity."

        team = self.VALID_TEAM[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.__find_equipment_by_type(equipment_type)
        team = self.__find_team_by_name(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.__find_team_by_name(team_name)
        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipments = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        for equipment in equipments:
            equipment.increase_price()

        return f"Successfully changed {len(equipments)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self.__find_team_by_name(team_name1)
        team2 = self.__find_team_by_name(team_name2)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + sum(e.price for e in team1.equipment)
        team2_points = team2.advantage + sum(e.price for e in team2.equipment)

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."

        if team2_points > team1_points:
            team2.win()
            return f"The winner is {team2.name}."

        return f"No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:"]
        [result.append(t.get_statistics()) for t in sorted_teams]

        return "\n".join(result)

    def __find_equipment_by_type(self, equipment_type):
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        return equipment[-1] if equipment else None

    def __find_team_by_name(self, team_name):
        team = [t for t in self.teams if t.name == team_name]
        return team[0] if team else None
