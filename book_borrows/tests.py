import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from library.models import Book
from users.models import BaseUser
from .models import Borrow


class BorrowTestCase(TestCase):
	def setUp(self):
		self.normal_user_2 = User.objects.create_user('user@gmail.com', 'user@gmail.com', 'user')
		self.base_user = BaseUser.objects.create(user=self.normal_user_2,
													name='Eduardo',
													last_name='Vaca',
													address='San Salvador 15 San Gil, qro.',
													age=20,
													phone='4271171443',
													sex='M')

		end_date = timezone.make_aware(datetime.datetime(2016, 3, 15))

		self.book_sombra = Book.objects.create(name='La sombra del viento')
		self.borrow_one = Borrow.objects.create(user=self.base_user,
												book=self.book_sombra,
												end_date=end_date,)

	def test_status(self):
		"""Tests if the status of the book borrowed is correct
		"""
		self.assertEqual(self.borrow_one.status, 'BO')
