from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    '''Create test cases for the models class'''

    def test_create_user_with_email_successful(self):
        '''Test that a new user is created with an email is successful'''
        email = "ovansa.im@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        '''Test new user is normalised'''
        email = "ovansa.im@GMAIL.com"
        user = get_user_model().objects.create_user(
            email,
            'password'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_no_email(self):
        '''Test new user with no email returns error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password")

    def test_create_new_superuser(self):
        '''Test creating a new create_superuser'''
        user = get_user_model().objects.create_superuser(
            "test@email.com",
            "password"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
