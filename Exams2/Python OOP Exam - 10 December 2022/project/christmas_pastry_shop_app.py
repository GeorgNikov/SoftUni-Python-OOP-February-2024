from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    VALID_DELICACY = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTH = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0.0
        # self.delicacies_name = set()
        # self.both_number = set()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.__find_delicacies_by_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved]

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth[0].reserve(number_of_people)
        return f"Booth {booth[0].booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        delicacy = self.__find_delicacies_by_name(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill

        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_delicacies_by_name(self, delicacies_name):
        delicacy = [d for d in self.delicacies if d.name == delicacies_name]
        return delicacy[0] if delicacy else None

    def __find_booth_by_number(self, both_number):
        booth = [b for b in self.booths if b.booth_number == both_number]
        return booth[0] if booth else None
