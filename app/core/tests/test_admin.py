from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        '''Setup client'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="ovansa@gmail.com",
            password="password"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="ov@gmail.com",
            password="password",
            name="Users Names Ova",
        )

    def test_for_users_listed(self):
        '''Test that users are listed'''
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_for_user_changed_page(self):
        '''Test that user edit page works'''
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        '''Test that the create user page works'''
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
