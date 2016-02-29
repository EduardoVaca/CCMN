from django.test import TestCase
from .models import Author, Category, Book, Wrote, Has


class AuthorTestCase(TestCase):
	def setUp(self):
		self.author = Author.objects.create(name='Carlos Ruiz Zafón')
		self.author2 = Author.objects.create(name='J.K. Rowling')
		self.category_love = Category.objects.create(name='Love')
		self.category_mistery = Category.objects.create(name='Mistery')
		self.book_sombra = Book.objects.create( name='La sombra del viento')
		Wrote.objects.create(author=self.author, book=self.book_sombra)
		Wrote.objects.create(author=self.author2, book=self.book_sombra)
		Has.objects.create(book=self.book_sombra, category=self.category_love)
		Has.objects.create(book=self.book_sombra, category=self.category_mistery)
		

	def test_author_str(self):
		"""Tests if the author is created and the name is correct
		"""
		self.assertEqual(self.author.name, 'Carlos Ruiz Zafón')

	def test_category_str(self):
		"""Tests if the category is created and the name is correct
		"""
		self.assertEqual(self.category_love.name, 'Love')
		self.assertEqual(self.category_mistery.name, 'Mistery')

	def test_book_str(self):
		"""Tests if the book is created and the name is correct
		"""
		self.assertEqual(self.book_sombra.name, 'La sombra del viento')

	def test_book_author(self):
		"""Tests if the book has the correct author
		"""
		self.assertEqual(self.book_sombra.authors.all()[0].name, 'Carlos Ruiz Zafón')
		self.assertEqual(len(self.book_sombra.authors.all()), 2)

	def test_book_category(self):
		"""Tests if the book has the correct categories
		"""
		self.assertEqual(self.book_sombra.categories.all()[0].name, 'Love')
		self.assertEqual(self.book_sombra.categories.all()[1].name, 'Mistery')
