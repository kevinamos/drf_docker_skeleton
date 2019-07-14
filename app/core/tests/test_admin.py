from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.clinet = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin1@gmail.com',
            password='pass12345'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test3@gmail.com',
            password='123test@90',
            name='Test user name here'
        )

    def test_users_list(self):
        url = reverse('admin')
        res = self.client.get(url)
        self.assertContains(res, self.user.name
                            )
        self.assertContains(res, self.user.email
                            )
