from unittest import TestCase, main
from project import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(145.5, 125.5)
        self.vehicle.capacity = 250
        self.vehicle.fuel_consumption = 1.25

    def test_correct_init(self):
        self.assertEqual(145.5, self.vehicle.fuel)
        self.assertEqual(125.5, self.vehicle.horse_power)
        self.assertEqual(250, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_is_not_enough_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1200)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive__when_enough_fuel_expect_decrease_fuel(self):
        self.vehicle.drive(100)

        self.assertEqual(20.5, self.vehicle.fuel)

    def test_refuel__when_fuel_more_than_capacity_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2000)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel__when_fuel_is_normal_capacity_expect_fuel_increase(self):
        self.vehicle.refuel(20)

        self.assertEqual(165.5, self.vehicle.fuel)

    def test__str__expected_string(self):
        result = 'The vehicle has 125.5 horse power with 145.5 fuel left and 1.25 fuel consumption'

        self.assertEqual(result, str(self.vehicle))


if __name__ == '__main__':
    main()
