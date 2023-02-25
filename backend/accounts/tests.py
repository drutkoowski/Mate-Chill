from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.login_url = reverse('accounts:token_obtain_pair')
        self.signup_url = reverse('accounts:register')

    def test_account_authentication(self):
        response = self.client.post(self.signup_url, {
            "email": "test123@o2.pl",
            "first_name": "Damian",
            "last_name": "Rutkowski",
            "phone": 123456789,
            "password": "test123"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(self.login_url, {
            "email": "test123@o2.pl",
            'password': 'test123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

