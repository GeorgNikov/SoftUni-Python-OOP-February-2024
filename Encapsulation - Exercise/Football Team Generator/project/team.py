from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating
        self.players: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        try:
            player_to_remove = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.players.remove(player_to_remove)
        return player_to_remove