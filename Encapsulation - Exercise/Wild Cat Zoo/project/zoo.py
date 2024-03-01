from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        worker = next(filter(lambda n: n.name == worker_name, self.workers))
        try:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = 0
        for worker in self.workers:
            total += worker.salary

        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = 0

        for animal in self.animals:
            total += animal.money_for_care

        if self.__budget >= total:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__get_obj_status_by_type('Lion', self.animals)
        result += self.__get_obj_status_by_type('Tiger', self.animals)
        result += self.__get_obj_status_by_type('Cheetah', self.animals)

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__get_obj_status_by_type('Keeper', self.workers)
        result += self.__get_obj_status_by_type('Caretaker', self.workers)
        result += self.__get_obj_status_by_type('Vet', self.workers)

        return result.strip()

    @staticmethod
    def __get_obj_status_by_type(object_type, object_list):
        objects = [str(x) for x in object_list if x.__class__.__name__ == object_type]

        result = f'----- {len(objects)} {object_type}s:\n'

        for obj in objects:
            result += f"{obj}\n"

        return result
