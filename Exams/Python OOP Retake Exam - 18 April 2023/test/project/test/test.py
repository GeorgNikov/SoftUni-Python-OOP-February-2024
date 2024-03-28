from project.robot import Robot
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self):
        self.robot = Robot('1', 'Military', 10, 1000)

    def test_correct_init(self):
        self.assertEqual('1', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertListEqual([], self.robot.hardware_upgrades)
        self.assertListEqual([], self.robot.software_updates)

    def test_category__setter_wrong_category_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Home'

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price__setter_negative_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual('Price cannot be negative!', str(ve.exception))

    def test_upgrade__existing_hardware_return_string(self):
        self.robot.hardware_upgrades.append('valve')
        result = self.robot.upgrade('valve', 100)

        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)

    def test_upgrade__not_existing_hardware_expect_increase_price_add_to_list_and_return_string(self):
        result = self.robot.upgrade('valve', 100)

        self.assertEqual(1150, self.robot.price)
        self.assertListEqual(['valve'], self.robot.hardware_upgrades)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with valve.', result)

    def test_update__older_version_return_string(self):
        self.robot.update(0.05, 1)
        result = self.robot.update(0.01, 1)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update__small_capacity_return_string(self):
        self.robot.update(0.05, 1)
        result = self.robot.update(0.06, 12)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update__success_expect_add_to_list_decrease_capacity_return_string(self):
        result = self.robot.update(0.05, 1)

        self.assertListEqual([0.05], self.robot.software_updates)
        self.assertEqual(9, self.robot.available_capacity)
        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 0.05.', result)

    def test__gt__if_price_is_bigger_return_string(self):
        self.robot2 = Robot('2', 'Military', 1, 1)
        self.robot3 = Robot('3', 'Entertainment', 1, 2)

        self.assertTrue(self.robot3.price > self.robot2.price)
        self.assertEqual(f'Robot with ID 3 is more expensive than Robot with ID 2.', self.robot3.__gt__(self.robot2))

    def test__gt__if_price_is_lower_return_string(self):
        self.robot2 = Robot('2', 'Military', 1, 1)
        self.robot3 = Robot('3', 'Entertainment', 1, 2)

        self.assertFalse(self.robot3.price < self.robot2.price)
        self.assertEqual(f'Robot with ID 2 is cheaper than Robot with ID 3.', self.robot2.__gt__(self.robot3))

    def test__gt__if_price_is_equal_return_string(self):
        self.robot2 = Robot('2', 'Military', 1, 2)
        self.robot3 = Robot('3', 'Entertainment', 1, 2)

        self.assertTrue(self.robot2.price == self.robot3.price)
        self.assertEqual(f'Robot with ID 2 costs equal to Robot with ID 3.', self.robot2.__gt__(self.robot3))


if __name__ == '__main__':
    main()
