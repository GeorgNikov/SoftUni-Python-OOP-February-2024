from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Pesho',
                         1,
                         77,
                         15
                         )

        self.enemy = Hero('Ivo',
                          1,
                          75,
                          12
                          )

    def test_correct_init(self):
        self.assertEqual('Pesho', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(77, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle__when_hero_fight_yourself_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__when_health_is_negative_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ve.exception))

    def test_battle__when_enemy_health_is_negative_raise_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual('You cannot fight Ivo. He needs to rest', str(ve.exception))

    def test_battle__when_result_draw_decreased_health(self):
        self.hero.health = 5
        self.enemy.health = 5

        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(-7, self.hero.health)
        self.assertEqual(-10, self.enemy.health)

    def test_battle__when_hero_win_expect_stats_increase(self):
        self.enemy.health = 5
        exp_level = self.hero.level + 1
        exp_health = self.hero.health - self.enemy.damage + 5
        exp_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual('You win', result)
        self.assertEqual(exp_level, self.hero.level)
        self.assertEqual(exp_health, self.hero.health)
        self.assertEqual(exp_damage, self.hero.damage)

    def test_battle__when_enemy_win_expect_stats_increase(self):
        self.hero, self.enemy = self.enemy, self.hero

        exp_level = self.enemy.level + 1
        exp_health = self.enemy.health - self.hero.damage + 5
        exp_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(exp_level, self.enemy.level)
        self.assertEqual(exp_health, self.enemy.health)
        self.assertEqual(exp_damage, self.enemy.damage)

    def test_correct__str__(self):
        exp_result = f"""Hero {self.hero.username}: {self.hero.level} lvl
Health: {self.hero.health}
Damage: {self.hero.damage}
"""
        self.assertEqual(exp_result, str(self.hero))


if __name__ == '__main__':
    main()
