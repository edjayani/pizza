from unittest import TestCase, main
from pizza import pizzas


class TestStringMethods(TestCase):

    def test_menu(self):
        ans = {'Margherita🧀': ['tomato sause', 'mozzarella', 'chicken', 'pineapples'],
         'Pepperoni🍕': ['tomato sause', 'mozzarella', 'chicken', 'pineapples'],
         'Hawaiian🍍': ['tomato sause', 'mozzarella', 'chicken', 'pineapples']}

        self.assertEqual(pizzas.menu_show(), ans)

    def test_size(self):
        self.assertNotEqual(pizzas.width('L'), 30)

    def test_wrong_size(self):
        with self.assertRaises(UnboundLocalError):
            pizzas.width('M')


if __name__ == '__main__':
    main()