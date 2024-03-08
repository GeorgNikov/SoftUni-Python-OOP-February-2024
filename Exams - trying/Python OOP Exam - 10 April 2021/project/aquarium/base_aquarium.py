class BaseAquarium:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decoration = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise "Aquarium name cannot be an empty string."

        self.__name = value

    def calculate_comfort(self):
        return sum(x.price for x in self.decoration)

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."

        fish_type = fish.__class__.__name__
        if fish_type in ("FreshwaterFish", "SaltwaterFish"):
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

        self.fish.append(fish)

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decoration.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        result = f"{self.name}\nFish: "
        if self.fish:
            result += " ".join(f.name for f in self.fish)
        else:
            result += "none\n"
        result += f"\nDecorations: {len(self.decoration)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result
