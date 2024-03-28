from project import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('model1', 'type1', 10000, 12_500)

    def test_correct__init_(self):
        self.assertEqual('model1', self.car.model)
        self.assertEqual('type1', self.car.car_type)
        self.assertEqual(10000, self.car.mileage)
        self.assertEqual(12500, self.car.price)
        self.assertListEqual([], self.car.repairs)

    def test_price_setter_with_wrong_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_with_wrong_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price__with_biggest_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(13000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price__with_correct_price_set_new_price_return_result(self):
        result = self.car.set_promotional_price(11000)

        self.assertEqual(11000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_when_bigger_repair_price_return_result(self):
        result = self.car.need_repair(10000, 'sensor')

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_when_correct_repair_price_expect_price_increase_and_add_description_return_result(self):
        result = self.car.need_repair(100, 'sensor')

        self.assertEqual(12600, self.car.price)
        self.assertListEqual(['sensor'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

    def test_need_repair_two_when_correct_repair_price_expect_price_increase_and_add_description_return_result(self):
        result = self.car.need_repair(100, 'sensor')

        self.assertEqual(12600, self.car.price)
        self.assertListEqual(['sensor'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

        result = self.car.need_repair(200, 'oil filter')

        self.assertEqual(12800, self.car.price)
        self.assertListEqual(['sensor', 'oil filter'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

    def test__gt__with_different_car_type_return_result(self):
        self.car2 = SecondHandCar('Model2', 'type2', 12000, 10000)
        result = self.car.__gt__(self.car2)

        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__with_same_car_type_return_result(self):
        self.car1 = SecondHandCar('model1', 'type1', 10000, 12000)
        self.car2 = SecondHandCar('model2', 'type1', 11000, 13000)

        self.assertFalse(self.car1 > self.car2)
        self.assertTrue(self.car2 > self.car1)

    def test_correct_str_one_repairs(self):
        self.car.need_repair(25, 'sensor')
        result = f"""Model model1 | Type type1 | Milage 10000km
Current price: 12525.00 | Number of Repairs: 1"""

        self.assertEqual(result, str(self.car))

    def test_correct_str_meny_repairs(self):
        self.car.need_repair(25, 'sensor')
        self.car.need_repair(125, 'motor')
        result = f"""Model model1 | Type type1 | Milage 10000km
Current price: 12650.00 | Number of Repairs: 2"""

        self.assertEqual(result, str(self.car))

    def test_correct_str_no_repairs(self):
        result = f"""Model model1 | Type type1 | Milage 10000km
Current price: 12500.00 | Number of Repairs: 0"""

        self.assertEqual(result, str(self.car))


if __name__ == '__main__':
    main()
