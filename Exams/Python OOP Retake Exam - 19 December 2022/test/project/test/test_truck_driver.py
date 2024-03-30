from project.truck_driver import TruckDriver
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self):
        self.td = TruckDriver('Ivan', 1)
        self.td_cargo = TruckDriver('Mitko', 1)

    def test_correct_init(self):
        self.assertEqual('Ivan', self.td.name)
        self.assertEqual(1, self.td.money_per_mile)
        self.assertDictEqual({}, self.td.available_cargos)
        self.assertEqual(0, self.td.earned_money)
        self.assertEqual(0, self.td.miles)

        self.td_cargo.available_cargos = {'cargo': 10}
        self.td_cargo.earned_money = 10
        self.td_cargo.miles = 10

        self.assertEqual('Mitko', self.td_cargo.name)
        self.assertEqual(1, self.td_cargo.money_per_mile)
        self.assertDictEqual({'cargo': 10}, self.td_cargo.available_cargos)
        self.assertEqual(10, self.td_cargo.earned_money)
        self.assertEqual(10, self.td_cargo.miles)

    def test_earned_money_negative_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.td.earned_money = -1

        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer__existing_location_raise_exception(self):
        self.td_cargo.add_cargo_offer('cargo', 500)
        with self.assertRaises(Exception) as ex:
            self.td_cargo.add_cargo_offer('cargo', 500)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer__new_location_expect_success(self):
        result = self.td.add_cargo_offer('Vienna', 500)

        self.assertEqual("Cargo for 500 to Vienna was added as an offer.", result)
        self.assertDictEqual({'Vienna': 500}, self.td.available_cargos)

    def test_drive_best_cargo_offer_if_no_offer_raise_value_error(self):
        result = self.td.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_if_3_offer_raise_value_error(self):
        self.td.add_cargo_offer('Germany', 1500)
        self.td.add_cargo_offer('France', 1430)
        self.td.add_cargo_offer("Bulgaria", 780)

        result = self.td.drive_best_cargo_offer()

        self.assertEqual("Ivan is driving 1500 to Germany.", result)
        self.assertEqual(835, self.td.earned_money)
        self.assertEqual(1500, self.td.miles)

    def test_eat(self):
        self.td.earned_money = 200

        self.td.eat(250)
        self.td.eat(500)

        self.assertEqual(160, self.td.earned_money)

    def test_sleep(self):
        self.td.earned_money = 200

        self.td.sleep(1000)
        self.td.sleep(2000)

        self.assertEqual(110, self.td.earned_money)

    def test_pump_gas(self):
        self.td.earned_money = 2000

        self.td.pump_gas(1500)
        self.td.pump_gas(3000)

        self.assertEqual(1000, self.td.earned_money)

    def test_repair_truck(self):
        self.td.earned_money = 16000

        self.td.repair_truck(10000)
        self.td.repair_truck(20000)

        self.assertEqual(1000, self.td.earned_money)

    def test__repr__no_cargo_expect_string(self):
        self.assertEqual("Ivan has 0 miles behind his back.", repr(self.td))

    def test__repr__with_cargo_expect_string(self):
        self.td.add_cargo_offer('Germany', 1500)
        self.td.add_cargo_offer('Vienna', 500)
        self.td.drive_best_cargo_offer()
        self.td.drive_best_cargo_offer()

        self.assertEqual("Ivan has 3000 miles behind his back.", repr(self.td))


if __name__ == '__main__':
    main()
