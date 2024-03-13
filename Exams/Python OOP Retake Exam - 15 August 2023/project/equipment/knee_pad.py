from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    TYPE_ = "KneePad"
    @property
    def get_price(self):
        return 15.0

    @property
    def get_protection(self):
        return 120

    def __init__(self):
        super().__init__(protection=self.get_protection, price=self.get_price)

    def increase_price(self):
        self.price *= 1.2       # Increase price with 20%