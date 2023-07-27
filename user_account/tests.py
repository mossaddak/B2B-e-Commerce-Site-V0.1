from django.test import TestCase
from .models import User


class UserAccountTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'mossaddak@gmail.com',
            'password': '1234',
            'first_name': 'Mossaddak',
            'last_name': 'Hossain'
        }

    def test_user_creation(self):
        user = User.objects.create(**self.user_data)

        self.assertEqual(user.email, self.user_data['email'], "Incorrect email for the created user.")
        self.assertEqual(user.password, self.user_data['password'], "Incorrect password for the created user.")
        self.assertEqual(user.first_name, self.user_data['first_name'], "Incorrect first name for the created user.")
        self.assertEqual(user.last_name, self.user_data['last_name'], "Incorrect last name for the created user.")

        users = User.objects.all()
        self.assertEqual(users.count(), 1, "Unexpected number of users created.")

    def tearDown(self):
        User.objects.all().delete()
