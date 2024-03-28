from unittest import TestCase, main
from project import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Miro', 'type1', 'sound1')

    def test_correct_init(self):
        self.assertEqual('Miro', self.mammal.name)
        self.assertEqual('type1', self.mammal.type)
        self.assertEqual('sound1', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound_expect_string(self):
        result = self.mammal.make_sound()

        self.assertEqual('Miro makes sound1', result)

    def test_get_kingdom__return_string(self):
        result = self.mammal.get_kingdom()

        self.assertEqual('animals', result)

    def test_info_expect_string(self):
        result = self.mammal.info()

        self.assertEqual('Miro is of type type1', result)


if __name__ == '__main__':
    main()
