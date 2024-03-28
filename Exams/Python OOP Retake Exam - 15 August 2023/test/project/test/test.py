from project import Trip
from unittest import TestCase, main


class Test(TestCase):

    def setUp(self):
        self.trip = Trip(10000, 1, False)
        self.trip2 = Trip(10000, 2, False)
        self.trip_family = Trip(10000, 4, True)

    def test_correct_init(self):
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(10000, self.trip2.budget)
        self.assertEqual(10000, self.trip_family.budget)

        self.assertEqual(1, self.trip.travelers)
        self.assertEqual(2, self.trip2.travelers)
        self.assertEqual(4, self.trip_family.travelers)

        self.assertFalse(self.trip.is_family)
        self.assertFalse(self.trip2.is_family)
        self.assertTrue(self.trip_family.is_family)

        self.assertDictEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertDictEqual({}, self.trip2.booked_destinations_paid_amounts)
        self.assertDictEqual({}, self.trip_family.booked_destinations_paid_amounts)


    def test_travelers__setter_wrong_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family__setter_invalid_return_false(self):
        self.trip.travelers = 1
        self.assertFalse(self.trip.is_family)

        self.trip_family.travelers = 4
        self.assertTrue(self.trip_family.is_family)

    def test_is_family__true_to_false_return_false(self):
        trip2 = Trip(500, 1, True)

        self.assertFalse(trip2.is_family)
        self.assertEqual(trip2.booked_destinations_paid_amounts, {})

    def test_book_a_trip__if_destination_not_exist_return_string(self):
        result = self.trip.book_a_trip('Ireland')

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip__if_destination_exist_but_budget_is_not_enough_return_string(self):
        self.trip.budget = 100
        result = self.trip.book_a_trip('Bulgaria')

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip__if_destination_exist_budget_is_enough_return_string(self):
        result = self.trip.book_a_trip('Bulgaria')

        self.assertDictEqual({'Bulgaria': 500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(9500, self.trip.budget)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9500.00', result)

    def test_book_a_trip__two_booking_budget_is_enough_return_string(self):
        result = self.trip.book_a_trip('Bulgaria')
        result2 = self.trip.book_a_trip('Australia')

        self.assertDictEqual({'Bulgaria': 500, 'Australia': 5700}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(3800, self.trip.budget)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9500.00', result)
        self.assertEqual(f'Successfully booked destination Australia! Your budget left is 3800.00', result2)

    def test_booking_status__if_no_booking_return_string(self):
        result = self.trip.booking_status()

        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}', result)

    def test_booking_status__if_booking_one_person_return_sorted_string(self):
        self.trip.book_a_trip('Bulgaria')

        expect_string = ("Booked Destination: Bulgaria\nPaid Amount: 500.00\n"
                         "Number of Travelers: 1\nBudget Left: 9500.00")

        self.assertEqual(expect_string, self.trip.booking_status())

    def test_booking_status__if_booking_two_person_return_sorted_string(self):
        self.trip.travelers = 2
        self.trip.book_a_trip('Bulgaria')

        expect_string = ("Booked Destination: Bulgaria\nPaid Amount: 1000.00\n"
                         "Number of Travelers: 2\nBudget Left: 9000.00")

        self.assertEqual(expect_string, self.trip.booking_status())


if __name__ == '__main__':
    main()
