from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self):
        self.tp = TennisPlayer('Test', 20, 5.5)

    def test_correct_init(self):
        self.assertEqual('Test', self.tp.name)
        self.assertEqual(20, self.tp.age)
        self.assertEqual(5.5, self.tp.points)
        self.assertListEqual([], self.tp.wins)

    def test_name__setter_wrong_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Al', 20, 0)  # From AS

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age__under_18_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Alex', 17, 0)    # From AS

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_when_name_already_in_list_expect_return_string(self):
        self.tp.wins.append('Tenis')
        result = self.tp.add_new_win('Tenis')

        self.assertEqual("Tenis has been already added to the list of wins!", result)

    def test_add_new_win__when_name_not_in_list_expect_add_name(self):
        result = self.tp.add_new_win('Tenis')

        self.assertIsNone(result)
        self.assertListEqual(['Tenis'], self.tp.wins)

    def test_add_new_win__2_tournaments_in_list_expect_add_name(self):
        result = self.tp.add_new_win('Tenis')
        result2 = self.tp.add_new_win('Tenis2')

        self.assertIsNone(result)
        self.assertIsNone(result2)
        self.assertListEqual(['Tenis', 'Tenis2'], self.tp.wins)

    def test__lt__return_string(self):
        t1 = TennisPlayer('TenisPlayer1', 20, 5.5)
        t2 = TennisPlayer('TenisPlayer2', 21, 6.5)

        self.assertTrue(t2.points > t1.points)
        self.assertEqual(f'{t2.name} is a better player than {t1.name}', t2.__lt__(t1))

    def test__lt__opposite_return_string(self):
        t1 = TennisPlayer('TenisPlayer1', 20, 7.5)
        t2 = TennisPlayer('TenisPlayer2', 21, 6.5)

        self.assertFalse(t2.points > t1.points)
        self.assertEqual(f'{t1.name} is a top seeded player and he/she is better than {t2.name}', t2.__lt__(t1))

    # From author solution

    def test__str__correct_no_wins(self):
        result = f"Tennis Player: {self.tp.name}\n" \
                 f"Age: {self.tp.age}\n" \
                 f"Points: {self.tp.points:.1f}\n" \
                 f"Tournaments won: "

        self.assertEqual(result, str(self.tp))

    def test__str__correct_1_win(self):
        self.tp.add_new_win('Tenis')

        result = f"Tennis Player: {self.tp.name}\n" \
                 f"Age: {self.tp.age}\n" \
                 f"Points: {self.tp.points:.1f}\n" \
                 f"Tournaments won: Tenis"

        self.assertEqual(result, str(self.tp))

    def test__str__correct_2_wins(self):
        self.tp.add_new_win('Tenis')
        self.tp.add_new_win('TenisUSA')

        result = f"Tennis Player: {self.tp.name}\n" \
                 f"Age: {self.tp.age}\n" \
                 f"Points: {self.tp.points:.1f}\n" \
                 f"Tournaments won: Tenis, TenisUSA"

        self.assertEqual(result, str(self.tp))


if __name__ == '__main__':
    main()
