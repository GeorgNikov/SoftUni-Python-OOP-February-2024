from project import Car


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def change_car(self, car: Car):
        car.is_taken = True
        if not self.car:
            self.car = car
            return f"Driver {self.name} chose the car {car.model}."

        self.car.is_taken = False
        old_model = self.car.model
        self.car = car
        return f"Driver {self.name} changed his car from {old_model} to {car.model}."
