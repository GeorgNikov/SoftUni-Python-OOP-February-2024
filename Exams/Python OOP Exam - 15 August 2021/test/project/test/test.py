from project import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    PET_SHOP = 'MyVet'
    FOOD_NAME = 'test_food'
    PET_NAME = 'Pepi'

    def setUp(self):
        self.shop = PetShop('MyVet')
        # self.shop.food = {}
        # self.shop.pets = []

    def test_correct_init(self):
        self.assertEqual(self.PET_SHOP, self.shop.name)
        self.assertDictEqual({}, self.shop.food)
        self.assertListEqual([], self.shop.pets)

    def test_add_food_negative_quantity_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food(self.FOOD_NAME, -3)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_if_food_name_not_in_food(self):
        self.shop.add_food(self.FOOD_NAME, 3)
        self.shop.add_food('Other', 13)

        self.assertEqual(3, self.shop.food[self.FOOD_NAME])
        self.assertEqual(13, self.shop.food['Other'])

    def test_add_food_success_expect_increase_quantity(self):
        self.shop.add_food(self.FOOD_NAME, 10)
        self.shop.add_food(self.FOOD_NAME, 15)

        self.assertEqual(25, self.shop.food[self.FOOD_NAME])

    def test_add_food_success_expect_correct_message(self):
        result = self.shop.add_food(self.FOOD_NAME, 10)

        self.assertEqual('Successfully added 10.00 grams of test_food.', result)

    def test_add_pet_when_pet_is_in_pets_list_expect_raise_exception(self):
        self.shop.add_pet(self.PET_NAME)

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet(self.PET_NAME)

        self.assertEqual('Cannot add a pet with the same name', str(ex.exception))

    def test_add_pet_when_pet_name_is_unique_expect_add_to_list_and_return_msg(self):
        result = self.shop.add_pet('Mimi')

        self.assertListEqual(['Mimi'], self.shop.pets)
        self.assertEqual('Successfully added Mimi.', result)

    def test_feed_pet__when_name_not_in_pets_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('Wiskas', 'Kaspar')

        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_pet__when_food_name_not_in_food_return_message(self):
        self.shop.add_pet('Mimi')
        result = self.shop.feed_pet('Salami', 'Mimi')

        self.assertEqual('You do not have Salami', result)

    def test_feed_pet__when_food_under_100_return_msg_increase_food(self):
        self.shop.food[self.FOOD_NAME] = 0
        self.shop.pets = ['Mimi']

        self.assertEqual('Adding food...', self.shop.feed_pet(self.FOOD_NAME, 'Mimi'))
        self.assertDictEqual({self.FOOD_NAME: 1000}, self.shop.food)

    def test_feed_pet__when_food_is_enough_decrease_food_and_return_message(self):
        self.shop.add_pet('Mimi')
        self.shop.add_food(self.FOOD_NAME, 500)
        msg = 'Mimi was successfully fed'

        self.assertEqual(msg, self.shop.feed_pet(self.FOOD_NAME, 'Mimi'))
        self.assertDictEqual({self.FOOD_NAME: 400}, self.shop.food)

    def test_repr__when_no_pets_expect_result(self):
        result = f'''Shop MyVet:
Pets: '''

        self.assertEqual(result, repr(self.shop))

    def test_repr__when_have_one_pet_expect_result(self):
        self.shop.add_pet('Mimi')
        result = f'''Shop MyVet:
Pets: Mimi'''

        self.assertEqual(result, repr(self.shop))

    def test_repr__when_have_more_pets_expect_result(self):
        self.shop.add_pet('Mimi')
        self.shop.add_pet('Victor')
        result = f'Shop {self.PET_SHOP}:\nPets: Mimi, Victor'

        self.assertEqual(result, repr(self.shop))


if __name__ == '__main__':
    main()
