from abc import ABC, abstractmethod
from project import BakedFood
from project import Drink


class Table(ABC):
    MIN_TABLE_NUMBER = None
    MAX_TABLE_NUMBER = None
    ERROR_MESSAGE = None

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.MIN_TABLE_NUMBER or value > self.MAX_TABLE_NUMBER:
            raise ValueError(self.ERROR_MESSAGE)
        self.__table_number = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, food: BakedFood):
        self.food_orders.append(food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result = (sum(f.price for f in self.food_orders) +
                  sum(d.price for d in self.drink_orders))
        return result

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f'''Table: {self.table_number}
Type: {self.__class__.__name__}
Capacity: {self.capacity}'''
