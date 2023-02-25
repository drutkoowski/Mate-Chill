from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.models import Account
from products.models import Product, Manufacturer, Category


class ProductTestCase(APITestCase):

    def setUp(self):
        self.products_list_url = reverse('products:products')
        self.user = Account.objects.create_user(email='test99@o2.pl', first_name='Test',
                                                last_name='Test', phone=123456789,
                                                password='test99'
                                                )
        self.manufacturer = Manufacturer.objects.create(name='Tester Manufacturer')
        self.category = Category.objects.create(name='Test Category')

    def authenticate(self):
        response = self.client.post(self.login_url, {
            "email": "test99@o2.pl",
            'password': 'test99'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_list(self):
        response = self.client.get(self.products_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_product(self):
        self.product = Product.objects.create(name='Product 123',
                                              num_available=12,
                                              manufacturer=self.manufacturer,
                                              price=123
                                              )
        product = Product.objects.get(name='Product 123')
        self.assertEqual(product.pk, self.product.pk)

    def test_create_invalid_product(self):
        self.product = Product.objects.create(num_available=12, price=123)
        product_count = Product.objects.filter(name='Product 123').count()
        self.assertEqual(product_count, 0)
