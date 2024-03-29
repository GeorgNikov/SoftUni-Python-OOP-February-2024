from collections import deque
from project.railway_station import RailwayStation
from unittest import TestCase, main


class Test(TestCase):

    def setUp(self):
        self.rs = RailwayStation('Bora')

    def test_correct_init(self):
        self.assertEqual('Bora', self.rs.name)
        self.assertEqual(deque([]), self.rs.arrival_trains)
        self.assertEqual(deque([]), self.rs.departure_trains)

    def test_wrong_name_length_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = 'TS'

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_expect_add_to_list(self):
        self.rs.new_arrival_on_board('Train1')

        self.assertEqual(deque(['Train1']), self.rs.arrival_trains)

    def test_new_arrival_nore_train_expect_add_to_list(self):
        self.rs.new_arrival_on_board('Train1')
        self.rs.new_arrival_on_board('Train2')

        self.assertEqual(deque(['Train1', 'Train2']), self.rs.arrival_trains)

    def test_train_has_arrived__not_from_deque_expect_string(self):
        self.rs.new_arrival_on_board('Train1')
        self.rs.new_arrival_on_board('Train2')

        result = self.rs.train_has_arrived('Train2')

        self.assertEqual(f"There are other trains to arrive before Train2.", result)

    def test_train_has_arrived__from_correct_deque_expect_string(self):
        self.rs.new_arrival_on_board('Train1')
        self.rs.new_arrival_on_board('Train2')

        result = self.rs.train_has_arrived('Train1')

        self.assertEqual("Train1 is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['Train2']), self.rs.arrival_trains)

    def test_train_has_left__wrong_order_expect_false(self):
        self.rs.departure_trains.append('Train1')
        self.rs.departure_trains.append('Train2')

        result = self.rs.train_has_left('Train2')

        self.assertFalse(result)
        self.assertEqual(deque(['Train1', 'Train2']), self.rs.departure_trains)

    def test_train_has_left__correct_order_expect_false(self):
        self.rs.departure_trains.append('Train1')
        self.rs.departure_trains.append('Train2')

        result = self.rs.train_has_left('Train1')

        self.assertTrue(result)
        self.assertEqual(deque(['Train2']), self.rs.departure_trains)


if __name__ == '__main__':
    main()
