from django.test import TestCase
from .models import Client, Order

class OrderModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
         first_name='Berry', last_name='Silva', email='berrysilva145@gmail.com'
        )
      self.order = Order.objects.create(
        client= self.client,
        delivery_address= '333 Main Str',
        total_price = 250.00
      )

    def test_order_creation(self)
        self.assertEqual(self.order.client.first_name, 'Berry')
        self.assertEqual(self.order.status, 'pending')
