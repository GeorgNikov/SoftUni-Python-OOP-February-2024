from project import BaseService


class SecondaryService(BaseService):
    SERVICE_CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, capacity=self.SERVICE_CAPACITY)

    def details(self):
        return (f"{self.name} Secondary Service:\n"
                f"Robots: {self._get_names()}")
