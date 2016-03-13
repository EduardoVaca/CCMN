from django.test import TestCase
from django.contrib.auth.models import User, Permission

from .models import AdminUser, BaseUser

class AdminUserTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		self.normal_user = User.objects.create_user('normal', 'normal@gmail.com', 'normal')
		self.normal_user_2 = User.objects.create_user('user@gmail.com', 'user@gmail.com', 'user')
		self.base_user = BaseUser.objects.create(user=self.normal_user_2,
													name='Eduardo',
													last_name='Vaca',
													address='San Salvador 15 San Gil, qro.',
													age=20,
													phone='4271171443',
													sex='M')

	def test_admin_user_group(self):
		"""Tests if the group for admin dashboard is assigned correctly
		"""
		admin_user = AdminUser.objects.create(user=self.user)
		self.assertIsNotNone(admin_user.user.groups.get(name='administrator'))
		self.assertEqual(str(admin_user), 'temporary')


	def test_base_user_group(self):
		"""Tests if the group for base user is assigned correctly
		"""
		self.assertIsNotNone(self.base_user.user.groups.get(name='usuario_base'))		



