from project import BaseEquipment


class ElbowPad(BaseEquipment):
    TYPE_ = "ElbowPad"
    @property
    def get_price(self):
        return 25.0

    @property
    def get_protection(self):
        return 90

    def __init__(self):
        super().__init__(protection=self.get_protection, price=self.get_price)

    def increase_price(self):
        self.price *= 1.1
