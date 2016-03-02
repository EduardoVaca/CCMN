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



