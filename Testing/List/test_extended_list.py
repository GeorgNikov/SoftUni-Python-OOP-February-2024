from unittest import TestCase, main
# from Testing.List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(2, 6.3, 7, 9, 'test')

    def test_list_ignore_not_int(self):
        self.assertEqual([2, 7, 9], self.i_list.get_data())

    def test_add_not_int_value_to_list_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(6.2)

        self.assertEqual('Element is not Integer', str(ve.exception))

    def test_add_int_value_to_list_return_data(self):
        result = [2, 7, 9, 1]
        self.i_list.add(1)

        self.assertEqual(result, self.i_list.get_data())

    def test_remove_index_out_or_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(6)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_remove_index_exist_index_return_removed_element(self):
        self.i_list.remove_index(1)

        self.assertEqual([2, 9], self.i_list.get_data())

    def test_get_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(10)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_get_valid_index(self):
        result = self.i_list.get(1)

        self.assertEqual(7, result)

    def test_insert_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(12, 0)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_valid_index_with_non_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 5.5)

        self.assertEqual('Element is not Integer', str(ve.exception))

    def test_insert_element_on_valid_index(self):
        self.i_list.insert(1, 0)

        self.assertEqual([2, 0, 7, 9], self.i_list.get_data())

    def test_get_biggest_number(self):
        result = self.i_list.get_biggest()

        self.assertEqual(9, result)

    def test_get_index_by_element(self):
        result = self.i_list.get_index(9)
        expected_result = 2

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
