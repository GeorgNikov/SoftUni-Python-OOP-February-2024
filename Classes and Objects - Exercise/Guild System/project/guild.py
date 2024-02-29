from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if not player.guild == Player.default_guild and not player.guild == self.name:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        # Option 1
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = Player.default_guild

        # Option 2
        # for plr in self.players:
        #     if plr.name == player_name:
        #         self.players.remove(plr)
        #         plr.guild = Player.default_guild
        #         return f"Player {player_name} has been removed from the guild."
        # return f"Player {player_name} is not in the guild."

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()

        return result

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
