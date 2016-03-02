from django.test import TestCase
from django.contrib.auth.models import User, Permission

from .models import AdminUser

class AdminUserTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		self.normal_user = User.objects.create_user('normal', 'normal@gmail.com', 'normal')

	def test_admin_user_group(self):
		"""Tests if the group for admin dashboard is assigned correctly
		"""
		admin_user = AdminUser.objects.create(user=self.user)
		self.assertIsNotNone(admin_user.user.groups.get(name='administrator'))
		self.assertEqual(str(admin_user), 'temporary')



