from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class Test(TestCase):

    def setUp(self):
        self.sc = ShoppingCart('Niko', 1000)

    def test_correct_init(self):
        self.assertEqual('Niko', self.sc.shop_name)
        self.assertEqual(1000, self.sc.budget)
        self.assertDictEqual({}, self.sc.products)

    def test_shop_name_start_with_small_letter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sc.shop_name = 'test'

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ex.exception))

    def test_shop_name_none_letter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sc.shop_name = 'Test0'

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ex.exception))

    def test_add_to_cart__biggest_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sc.add_to_cart('Test', 100)

        self.assertEqual('Product Test cost too much!', str(ex.exception))

    def test_add_to_cart__to_biggest_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sc.add_to_cart('Test', 101)

        self.assertEqual('Product Test cost too much!', str(ex.exception))

    def test_add_to_cart__correct_value_expect_success(self):
        result = self.sc.add_to_cart('Test', 30)

        self.assertEqual('Test product was successfully added to the cart!', result)
        self.assertEqual(self.sc.products['Test'], 30)

    def test_remove_from_cart_wrong_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sc.remove_from_cart('test')

        self.assertEqual('No product with name test in the cart!', str(ex.exception))

    def test_remove_from_cart__correct_product_expect_succes(self):
        self.sc.add_to_cart('test', 10)
        result = self.sc.remove_from_cart('test')

        self.assertEqual('Product test was successfully removed from the cart!', result)
        self.assertEqual({}, self.sc.products)

    def test_remove_from_cart__two_correct_product_expect_success(self):
        self.sc.add_to_cart('test', 10)
        self.sc.add_to_cart('testA', 20)
        result = self.sc.remove_from_cart('test')

        self.assertEqual('Product test was successfully removed from the cart!', result)
        self.assertEqual({'testA': 20}, self.sc.products)

    def test__add__two_instance_expect_success(self):
        cart1 = ShoppingCart("ShopA", 500)
        cart1.add_to_cart("Product1", 50)
        cart1.add_to_cart("Product2", 30)

        cart2 = ShoppingCart("ShopB", 700)
        cart2.add_to_cart("Product3", 40)
        cart2.add_to_cart("Product4", 60)

        new_cart = cart1 + cart2

        self.assertEqual(new_cart.shop_name, "ShopAShopB")
        self.assertEqual(new_cart.budget, 1200)

        expected_products = {
            "Product1": 50,
            "Product2": 30,
            "Product3": 40,
            "Product4": 60
        }
        self.assertDictEqual(new_cart.products, expected_products)

    def test_buy_products_expect_succes(self):
        cart = ShoppingCart("MyShop", 100)
        cart.add_to_cart("Product1", 50)
        cart.add_to_cart("Product2", 30)
        result = cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 80.00lv.", result)

    def test_buy_products_over_budget(self):
        cart = ShoppingCart("MyShop", 50)
        cart.add_to_cart("Product1", 30)
        cart.add_to_cart("Product2", 40)
        with self.assertRaises(ValueError) as ex:
            cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 20.00lv!", str(ex.exception))


if __name__ == '__main__':
    main()
