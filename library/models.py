from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Books'


class Author(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Authors'


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'


class Wrote(models.Model):
	author = models.ForeignKey(Author)
	book = models.ForeignKey(Book)

	def __str__(self):
		return '%s - %s' % (self.author.name, self.book.name)


class Has(models.Model):
	book = models.ForeignKey(Book)
	category = models.ForeignKey(Category)

	def __str__(self):
		return '%s - %s' % (self.book.name, self.category.name)



