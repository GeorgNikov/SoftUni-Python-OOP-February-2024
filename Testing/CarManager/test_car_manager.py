from unittest import TestCase, main
# from Testing.CarManager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Ford', 'Focus', 10, 50)

    def test_valid_init(self):
        self.assertEqual('Ford', self.car.make)
        self.assertEqual('Focus', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_model_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_fuel_consumption_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_fuel_capacity_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel_with_negative_raise_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_valid_amount(self):
        self.car.refuel(150)

        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_without_fuel_rice_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_needed_fuel_amount(self):
        self.car.fuel_amount = 50
        self.car.drive(100)

        self.assertEqual(40, self.car.fuel_amount)


if __name__ == '__main__':
    main()
