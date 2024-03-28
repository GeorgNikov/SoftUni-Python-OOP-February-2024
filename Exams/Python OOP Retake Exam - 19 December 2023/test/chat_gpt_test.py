import unittest
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'TypeA', 100, 200)

    def test_category_property(self):
        self.assertEqual(self.robot.category, 'Mountain')
        with self.assertRaises(ValueError):
            self.robot.category = 'InvalidCategory'

    def test_get_used_capacity(self):
        self.assertEqual(self.robot.get_used_capacity(), 0)

    def test_get_available_capacity(self):
        self.assertEqual(self.robot.get_available_capacity(), 100)

    def test_get_used_memory(self):
        self.assertEqual(self.robot.get_used_memory(), 0)

    def test_get_available_memory(self):
        self.assertEqual(self.robot.get_available_memory(), 200)

    def test_install_software_success(self):
        software = {'name': 'SoftwareA', 'capacity_consumption': 50, 'memory_consumption': 100}
        self.assertEqual(self.robot.install_software(software),
                         "Software 'SoftwareA' successfully installed on Mountain part.")

    def test_install_software_failure_capacity(self):
        software = {'name': 'SoftwareB', 'capacity_consumption': 150, 'memory_consumption': 100}
        self.assertEqual(self.robot.install_software(software),
                         "Software 'SoftwareB' cannot be installed on Mountain part.")

    def test_install_software_failure_memory(self):
        software = {'name': 'SoftwareC', 'capacity_consumption': 50, 'memory_consumption': 300}
        self.assertEqual(self.robot.install_software(software),
                         "Software 'SoftwareC' cannot be installed on Mountain part.")

    def test_install_software_failure_both(self):
        software = {'name': 'SoftwareD', 'capacity_consumption': 150, 'memory_consumption': 300}
        self.assertEqual(self.robot.install_software(software),
                         "Software 'SoftwareD' cannot be installed on Mountain part.")


if __name__ == '__main__':
    unittest.main()
