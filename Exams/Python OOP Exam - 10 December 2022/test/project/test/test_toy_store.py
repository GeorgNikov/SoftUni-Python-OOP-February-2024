from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.ts = ToyStore()

    def test_add_toy__wrong_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('T', 'Train')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy__correct_shelf_exist_toy_raise_exception(self):
        self.ts.add_toy('D', 'Doll')

        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('D', 'Doll')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy__correct_shelf_already_taken_raise_exception(self):
        self.ts.add_toy('D', 'Doll')

        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('D', 'Drill')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy__correct_expect_success(self):
        result = self.ts.add_toy('D', 'Drill')

        self.assertEqual(self.ts.toy_shelf["D"], "Drill")
        self.assertEqual("Toy:Drill placed successfully!", result)

    def test_remove_toy__wrong_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy('T', 'Train')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy__wrong_toy_raise_exception(self):
        self.ts.add_toy('D', 'Drill')
        with self.assertRaises(Exception)as ex:
            self.ts.remove_toy('D', "Doll")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy__expect_success(self):
        self.ts.add_toy('D', 'Doll')
        result = self.ts.remove_toy('D', 'Doll')

        self.assertEqual("Remove toy:Doll successfully!", result)
        self.assertIsNone(self.ts.toy_shelf["D"])


if __name__ == '__main__':
    main()
