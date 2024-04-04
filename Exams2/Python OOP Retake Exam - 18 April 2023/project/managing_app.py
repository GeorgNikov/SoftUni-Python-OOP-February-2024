from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.__find_user_by_dln(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.__find_vehicle_by_lpn(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self.__find_route_by_start_and_end_point(start_point, end_point)
        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.length > length:
                route.is_locked = True

        new_route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, new_route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.__find_user_by_dln(driving_license_number)
        vehicle = self.__find_vehicle_by_lpn(license_plate_number)
        route = self.__find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = f"*** E-Drive-Rent ***\n"
        result += '\n'.join(str(u) for u in sorted_users)

        return result

    def __find_user_by_dln(self, driving_license_number):
        user = [u for u in self.users if u.driving_license_number == driving_license_number]
        return user[0] if user else None

    def __find_vehicle_by_lpn(self, license_plate_number):
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        return vehicle[0] if vehicle else None

    def __find_route_by_start_and_end_point(self, start_point, end_point):
        route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point]
        return route[0] if route else None

    def __find_route_by_id(self, route_id):
        route = [r for r in self.routes if r.route_id == route_id]
        return route[0] if route else None
