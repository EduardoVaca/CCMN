from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group


class AdminUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	def save(self, *args, **kwargs):
		"""Assign the admin user the group to enter to admin_dashboard
		"""
		admin_group = Group.objects.get_or_create(name='administrator')[0]
		self.user.groups.add(admin_group)		
		return super(AdminUser, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'AdminUsers'


class BaseUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	age = models.IntegerField(null=False)

	SEX_MALE = 'M'
	SEX_FEMALE = 'F'

	sex_choices = (
			(SEX_MALE, 'Hombre'),
			(SEX_FEMALE, 'Mujer')
		)
	sex = models.CharField(max_length=1,
							choices=sex_choices)

	def save(self, *args, **kwargs):
		"""Assign user into BaseUser group
		"""
		base_group = Group.objects.get_or_create(name='usuario_base')[0]
		self.user.groups.add(base_group)
		return super(BaseUser, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'BaseUsers'



