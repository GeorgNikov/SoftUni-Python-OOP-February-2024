from typing import List
from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str = None):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        # Option 1
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

        # Option 2
        # for i, name in enumerate(self.pokemons):
        #     if pokemon_name == name.name:
        #         del self.pokemons[i]
        #         return f"You have released {pokemon_name}"
        # return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"

        for info in self.pokemons:
            result += f"- {info.pokemon_details()}\n"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
