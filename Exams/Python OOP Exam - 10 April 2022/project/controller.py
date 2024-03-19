from project.player import Player


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def _get_player_by_name(self, name):
        player = [p for p in self.players if p.name == name]
        return player[0]

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def add_player(self, *players):
        added_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._get_player_by_name(player_name)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self._get_player_by_name(first_player_name)
        player2 = self._get_player_by_name(second_player_name)

        error = ''
        if player1.stamina == 0:
            error += f"Player {player1.name} does not have enough stamina."
        if player2.stamina == 0:
            error += '\n' + f"Player {player2.name} does not have enough stamina."

        if error:
            return error.strip()

        if player2.stamina < player1.stamina:
            player1, player2 = player2, player1

        attacker_damage = player1.stamina / 2
        player2.stamina = max(player2.stamina - attacker_damage, 0)
        if player2.stamina == 0:
            return f"Winner: {player1.name}"

        defender_damage = player2.stamina / 2
        player1.stamina = max(player1.stamina - defender_damage, 0)
        if player1.stamina == 0:
            return f"Winner: {player2.name}"

        winner = player1 if player1.stamina > player2.stamina else player2

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), Player.STAMINA_MIN)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result
