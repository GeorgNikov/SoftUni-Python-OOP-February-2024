from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._get_user_by_license_number(driving_license_number)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._get_vehicle_by_license_number(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self._create_vehicle(vehicle_type, brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self._get_route_no_length(start_point, end_point)

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes)+1)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str,
                  license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = self._get_user_by_license_number(driving_license_number)
        vehicle = self._get_vehicle_by_license_number(license_plate_number)
        route = self._get_route_by_id(route_id)

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
            vehicle.battery_level = 100

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***", ]
        sorted_users = sorted(self.users, key=lambda user: user.rating, reverse=True)
        result.append(('\n'.join(str(user) for user in sorted_users)))
        return '\n'.join(result)

    # Helping methods

    def _get_user_by_license_number(self, license_number):
        user = [u for u in self.users if u.driving_license_number == license_number]
        return user[0] if user else None

    def _get_vehicle_by_license_number(self, license_number):
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_number]
        return vehicle[0] if vehicle else None

    def _get_route(self, start_point, end_point, length):
        route = [r for r in self.routes if r.start_point == start_point
                 and r.end_point == end_point and r.length == length]
        return route[0] if route else None

    def _get_route_by_id(self, route_id):
        route = [r for r in self.routes if r.route_id == route_id]
        return route[0] if route else None

    def _get_route_no_length(self, start_point, end_point):
        route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point]
        return route[0] if route else None

    def _create_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        return self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)
