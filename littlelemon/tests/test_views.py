from django.test import TestCase, Client
from restaurant.models import Menu
from django.contrib.auth.models import User



class MenuViewTest(TestCase):

    def setUp(self):
        self.menu1 = Menu.objects.create(
            id=1, title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(
            id=2, title="CottonCandy", price=90, inventory=200)

    def test_getall(self):
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/api/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)
