from unittest import TestCase, main
from custom_HashTable import HashTable


class Test(TestCase):
    def setUp(self):
        self.h = HashTable()

    def test_correct_init(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_count(self):
        result = self.h.count
        self.assertEqual(result, 0)

    # TODO more tests

if __name__ == '__main__':
    main()
