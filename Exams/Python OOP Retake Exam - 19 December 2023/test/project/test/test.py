from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', 'part', 5, 100)
        self.robot_soft = ClimbingRobot('Alpine', 'part', 5, 100)
        self.robot_soft.installed_software = [
            {'name': 'Python', 'capacity_consumption': 2, 'memory_consumption': 50},
            {'name': 'Python2', 'capacity_consumption': 2, 'memory_consumption': 50}
        ]

    def test_correct_init(self):
        self.assertEqual('Alpine', self.robot.category)
        self.assertEqual('part', self.robot.part_type)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertListEqual([], self.robot.installed_software)

    def test_category__wrong_category_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r1 = ClimbingRobot('New Category', 'part', 1, 1)

        self.assertEqual(f"Category should be one of {ClimbingRobot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity__when_no_consumption_return_total_consumption_zero(self):
        result = self.robot.get_used_capacity()

        self.assertEqual(0, result)

    def test_get_used_capacity__when_one_consumption_return_total_consumption(self):
        result = self.robot_soft.get_used_capacity()

        self.assertEqual(4, result)

    def test_get_available_capacity_no_software_return_capacity(self):
        result = self.robot_soft.get_available_capacity()

        self.assertEqual(1, result)

    def test_get_used_memory_expect_success(self):
        result = self.robot.get_used_memory()

        self.assertEqual(0, result)

    def test_get_available_memory_expect_success(self):
        result = self.robot_soft.get_available_memory()

        self.assertEqual(0, result)

    def test_install_software__with_max_equal_values_expect_success(self):
        result = self.robot.install_software(
            {'name': 'Python', 'capacity_consumption': 5, 'memory_consumption': 100}
        )

        self.assertEqual(f"Software 'Python' successfully installed on Alpine part.", result)
        self.assertEqual([{'name': 'Python', 'capacity_consumption': 5, 'memory_consumption': 100}],
                         self.robot.installed_software)

    def test_install_software__with_biggest_capacity_consumption_expect_success(self):
        result = self.robot.install_software(
            {'name': 'Python', 'capacity_consumption': 15, 'memory_consumption': 100}
        )

        self.assertEqual("Software 'Python' cannot be installed on Alpine part.", result)

    def test_install_software__with_biggest_memory_consumption_expect_success(self):
        result = self.robot.install_software(
            {'name': 'Python', 'capacity_consumption': 5, 'memory_consumption': 150}
        )

        self.assertEqual("Software 'Python' cannot be installed on Alpine part.", result)

    def test_install_software__with_biggest_capacity_and_memory_consumption_expect_success(self):
        result = self.robot.install_software(
            {'name': 'Python', 'capacity_consumption': 15, 'memory_consumption': 150}
        )

        self.assertEqual("Software 'Python' cannot be installed on Alpine part.", result)


if __name__ == '__main__':
    main()
