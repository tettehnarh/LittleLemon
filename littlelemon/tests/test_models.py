from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)
        item = str(menu_item)
        self.assertEqual(item, "IceCream : 80")
