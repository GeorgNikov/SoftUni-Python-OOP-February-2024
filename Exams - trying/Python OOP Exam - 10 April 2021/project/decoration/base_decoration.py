class BaseDecoration:

    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    def __repr__(self):
        return f"{self.comfort} - {self.price}"
