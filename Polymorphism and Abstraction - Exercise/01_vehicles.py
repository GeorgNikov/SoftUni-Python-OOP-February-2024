from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITION_INCREASE = 0.9

    def drive(self, distance):
        total_fuel_consumption = (self.fuel_consumption + self.AIR_CONDITION_INCREASE) * distance

        if self.fuel_quantity >= total_fuel_consumption:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_TANK_CAPACITY = 0.95
    AIR_CONDITION_INCREASE = 1.6

    def drive(self, distance):
        total_fuel_consumption = (self.fuel_consumption + self.AIR_CONDITION_INCREASE) * distance
        if self.fuel_quantity >= total_fuel_consumption:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_TANK_CAPACITY


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
