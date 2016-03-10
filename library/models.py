from __future__ import unicode_literals

from django.db import models


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


class Book(models.Model):
	name = models.CharField(max_length=255)
	authors = models.ManyToManyField(Author)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Books'
