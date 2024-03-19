from project.supply.supply import Supply


class Player:
    STAMINA_MAX = 100
    STAMINA_MIN = 0
    MIN_AGE = 12
    players_names = []

    def __init__(self, name, age, stamina=STAMINA_MAX):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        elif value in self.players_names:
            raise Exception(f"Name {value} is already used!")
        self.players_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.STAMINA_MIN or value > self.STAMINA_MAX:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.STAMINA_MAX

    def _sustain_player(self, supply: Supply):
        self.stamina = min(self.stamina + supply.energy, self.STAMINA_MAX)

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
