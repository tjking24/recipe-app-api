from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        # setup will run before the tests are run
        self.client = Client()
        # definnig self.client so can be used in other tests
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        # force_login users client helper function, will log user in
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test user full name'
            )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # use the test client to perfrom http get request to url
        # res is an object

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/user.id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
