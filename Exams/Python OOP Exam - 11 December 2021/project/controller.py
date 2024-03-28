from project import MuscleCar
from project import SportsCar
from project import Driver
from project import Race


class Controller:
    VALID_CARS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if self._find_car_by_model(model):
            raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CARS:
            new_car = self.VALID_CARS[car_type](model, speed_limit)
            self.cars.append(new_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self._find_last_car_by_type(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self._find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if any(d.name == driver.name for d in race.drivers):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(self.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # Start race
        winners = sorted(race.drivers, key=lambda d: d.car.speed_limit, reverse=True)

        result = []
        counter = 0
        for driver in winners:
            if counter == 3:
                break
            else:
                result.append(f"Driver {driver.name} wins the {race_name} "
                              f"race with a speed of {driver.car.speed_limit}.")
                counter += 1
                driver.number_of_wins += 1

        return '\n'.join(result)

    def _find_driver_by_name(self, driver_name):
        driver = [d for d in self.drivers if d.name == driver_name]
        return driver[0] if driver else None

    def _find_car_by_model(self, model):
        car = [c for c in self.cars if c.model == model]
        return car[0] if car else None

    def _find_race_by_name(self, race_name):
        race = [r for r in self.races if r.name == race_name]
        return race[0] if race else None

    def _find_last_car_by_type(self, car_type):
        car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        return car[-1] if car else None
