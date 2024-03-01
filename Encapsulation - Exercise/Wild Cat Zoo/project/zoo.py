class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal, price: int) -> str:
        price = int(price)
        if self.animal_capacity > len(self.animals) and price > self.budget:
            return "Not enough budget"

        if price <= self.budget and self.animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if len(self.workers) < self.workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:

        try:
            worker = next(filter(lambda n: n.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total = sum([x.salary for x in self.workers])

        if self.budget >= total:
            self.budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total = sum([x.money_for_care for x in self.animals])

        if self.budget >= total:
            self.budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        result += self.__get_obj_status_by_type('Lion', self.animals)
        result += self.__get_obj_status_by_type('Tiger', self.animals)
        result += self.__get_obj_status_by_type('Cheetah', self.animals)

        return result.strip()

    def workers_status(self) -> str:
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
