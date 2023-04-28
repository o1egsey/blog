from django.test import TestCase
from account.models import UserBase


class UserBaseModelTest(TestCase):

    def setUp(self):
        self.user = UserBase.objects.create_user(
            user_name='test_user',
            email='test_user@example.com',
            password='test_password'
        )

    def test_create_user(self):
        user = self.user
        user_name = 'test_user'
        email = 'test_user@example.com'
        self.assertEqual(user.email, email)
        self.assertEqual(user.user_name, user_name)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = 'admin@example.com'
        user_name = 'admin'
        password = 'password'
        superuser = UserBase.objects.create_superuser(
            email=email, user_name=user_name, password=password)
        self.assertEqual(superuser.email, email)
        self.assertEqual(superuser.user_name, user_name)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_str(self):
        user_name = 'testuser'
        user = UserBase.objects.create_user(
            email='testuser@example.com', user_name=user_name, password='password')
        self.assertEqual(str(user), user_name)

    def tearDown(self):
        self.user.delete()
