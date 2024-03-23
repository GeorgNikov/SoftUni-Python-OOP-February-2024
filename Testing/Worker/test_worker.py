from unittest import TestCase, main
from Testing.Worker.worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Gogo", 1000, 100)

    def test_init(self):
        self.assertEqual("Gogo", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_go_to_work_when_energy_under_null(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_when_have_energy_expect_increase_money_and_decrease_energy(self):
        self.worker.energy = 100
        expected_money = self.worker.salary * 3
        expected_energy = self.worker.energy - 3

        self.worker.work()
        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_expected_energy_increase_by_one(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_return_string(self):
        string = self.worker.get_info()
        self.assertEqual(f'Gogo has saved 0 money.', string)


if __name__ == "__main__":
    main()
