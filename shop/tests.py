from django.test import TestCase

from shop.models import *

class TestDataBase(TestCase):
    fixtures = [
        "shop/fixtures/data.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='root')

    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 1)
        self.assertEqual(user.username, 'root')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('123'))

    def  test_all_data(self):
        self.assertGreater(Product.object.all().count, 0)
        self.assertGreater(Order.object.all().count, 0)
        self.assertGreater(OrderItem.object.all().count, 0)
        self.assertGreater(Payment.object.all().count, 0)
    