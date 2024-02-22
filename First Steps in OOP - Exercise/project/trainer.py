from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name=None):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon.name not in [x.name for x in self.pokemons]:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for i, name in enumerate(self.pokemons):
            if pokemon_name == name.name:
                del self.pokemons[i]
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"

        for info in self.pokemons:
            result += f"- {info.pokemon_details()}\n"

        return result