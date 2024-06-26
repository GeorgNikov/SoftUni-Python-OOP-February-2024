from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOTS_TYPE = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES_TYPES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS_TYPE:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS_TYPE[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        if robot.SERVICE_TYPE != service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        self.robots.append(robot[0])
        service.robots.remove(robot[0])

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)

    def __find_robot_by_name(self, robot_name):
        robot = [r for r in self.robots if r.name == robot_name]
        return robot[0] if robot else None

    def __find_service_by_name(self, service_name):
        service = [s for s in self.services if s.name == service_name]
        return service[0] if service else None
