from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.models import Account
from orders.models import Order, OrderProduct
from products.models import Product, Manufacturer, Category


class ReviewTestCase(APITestCase):

    def setUp(self):
        self.login_url = reverse('accounts:token_obtain_pair')
        self.review_create_url = reverse('reviews:create')
        self.review_list_url = reverse('reviews:list')
        self.user = Account.objects.create_user(email='test99@o2.pl', first_name='Test',
                                                last_name='Test', phone=123456789,
                                                password='test99'
                                                )
        self.manufacturer = Manufacturer.objects.create(name='Tester Manufacturer')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Product 123',
                                              num_available=12,
                                              manufacturer=self.manufacturer,
                                              price=123
                                              )
        self.order = Order.objects.create(user=self.user, total_product_cost=123,
                                          shipping_cost=123,
                                          summary_cost=123,
                                          first_name='Test name',
                                          last_name='Test name',
                                          address='Test address',
                                          city_code='12-345',
                                          status='opłacone'
                                          )
        self.product_order = OrderProduct.objects.create(product=self.product, count=2,
                                                         price=12,
                                                         order=self.order
                                                         )

    def authenticate(self):
        response = self.client.post(self.login_url, {
            "email": "test99@o2.pl",
            'password': 'test99'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_create(self):
        self.authenticate()
        response = self.client.post(self.review_create_url, {
            'product': self.product.pk,
            'content': 'Super produkt!',
            'stars': 5,
            'author': self.user.pk
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_review_create_not_bought_item(self):
        self.authenticate()
        response = self.client.post(self.review_create_url, {
            'product': 999,
            'content': 'Super produkt!',
            'stars': 5,
            'author': self.user.pk
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_list(self):
        self.authenticate()
        response = self.client.get(self.review_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
