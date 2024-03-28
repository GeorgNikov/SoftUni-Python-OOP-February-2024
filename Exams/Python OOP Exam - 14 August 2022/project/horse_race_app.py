from project import HorseRace
from project import Appaloosa
from project import Thoroughbred
from project import Jockey


class HorseRaceApp:
    HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def _get_horse_by_name(self, horse_name):
        horse = [h for h in self.horses if h.name == horse_name]
        return horse[0] if horse else None

    def _get_jockey_by_name(self, jockey_name):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        return jockey[0] if jockey else None

    def _get_race_by_type(self, race_type):
        race = [r for r in self.horse_races if r.race_type == race_type]
        return race[0] if race else None

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self._get_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSE_TYPES:
            new_horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self._get_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = next(filter(lambda h: type(h).__name__ == horse_type and not h.is_taken, reversed(self.horses)))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._get_race_by_type(race_type)
        jockey = self._get_jockey_by_name(jockey_name)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._get_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = None

        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey

        return (f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")