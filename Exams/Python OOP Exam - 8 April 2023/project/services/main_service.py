from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, capacity=self.SERVICE_CAPACITY)

    def details(self):
        return (f"{self.name} Main Service:\n"
                f"Robots: {self._get_names()}")
