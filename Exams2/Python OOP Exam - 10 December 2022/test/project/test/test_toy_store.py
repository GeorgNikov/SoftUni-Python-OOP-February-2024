from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def test_initializes_toy_store_with_empty_dictionary(self):
        toy_store = ToyStore()
        expected_toy_shelf = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(toy_store.toy_shelf, expected_toy_shelf)

    def test_add_toy_empty_shelf(self):
        toy_store = ToyStore()
        shelf = "A"
        toy_name = "Teddy Bear"
        expected_result = "Toy:Teddy Bear placed successfully!"

        result = toy_store.add_toy(shelf, toy_name)

        self.assertEqual(result, expected_result)
        self.assertEqual(toy_store.toy_shelf[shelf], toy_name)

    def test_toy_already_in_shelf(self):
        toy_store = ToyStore()
        shelf = "A"
        toy_name = "Teddy Bear"
        toy_store.add_toy(shelf, toy_name)

        with self.assertRaises(Exception) as es:
            toy_store.add_toy(shelf, toy_name)

        self.assertEqual(str(es.exception), "Toy is already in shelf!")

    def test_add_toy_non_empty_shelf(self):
        toy_store = ToyStore()
        shelf = "A"
        toy_name_1 = "Teddy Bear"

        expected_result_1 = "Toy:Teddy Bear placed successfully!"
        expected_result_2 = "Shelf is already taken!"

        result_1 = toy_store.add_toy(shelf, toy_name_1)
        self.assertEqual(result_1, expected_result_1)

        with self.assertRaises(Exception) as ex:
            toy_store.add_toy('A', 'New Toy')

        self.assertEqual(expected_result_2, str(ex.exception))

    def test_add_toy_nonexistent_shelf(self):
        toy_store = ToyStore()
        shelf = "H"
        toy_name = "Robot"

        with self.assertRaises(Exception) as es:
            toy_store.add_toy(shelf, toy_name)

        self.assertEqual(str(es.exception), "Shelf doesn't exist!")

    def test_remove_toy_raises_exception_when_shelf_doesnt_exist(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as es:
            toy_store.remove_toy("H", "Teddy Bear")
        self.assertEqual(str(es.exception), "Shelf doesn't exist!")

    def test_remove_toy_raises_exception_when_shelf_exists_but_doesnt_have_toy(self):
        toy_store = ToyStore()
        toy_store.add_toy("A", "Teddy Bear")
        with self.assertRaises(Exception) as es:
            toy_store.remove_toy("A", "Robot")
        self.assertEqual(str(es.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual("Teddy Bear", toy_store.toy_shelf["A"])

    def test_remove_toy_successfully_when_shelf_and_toy_exist(self):
        toy_store = ToyStore()
        toy_store.add_toy("A", "Teddy Bear")
        result = toy_store.remove_toy("A", "Teddy Bear")
        self.assertEqual(result, "Remove toy:Teddy Bear successfully!")
        self.assertEqual(None, toy_store.toy_shelf["A"])


if __name__ == '__main__':
    main()
