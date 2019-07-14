from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'testkev@gmail.com'
        password = 'Rmbki78@9'
        user = get_user_model().objects.create(email=email, password=password)
        self.assertEqual(user.email, email)
        # self.assertTrue(user.check_password(password))

    """def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create(email=None, 
            password='9i09ioj09098')
            """

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'admin@gmail.com',
            'admin12344'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
