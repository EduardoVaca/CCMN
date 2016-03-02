from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission


class AdminUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	def save(self, *args, **kwargs):
		"""Assign the admin user the permision to enter to admin_dashboard
		"""
		content_type = ContentType.objects.get_for_model(settings.AUTH_USER_MODEL)
		admin_permission = Permission.objects.get_or_create(codename='admin_dashboard', 
															name='Admin Dashboard', 
															content_type=content_type)[0]
		self.user.user_permissions.add(admin_permission)
		return super(AdminUser, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'AdminUsers'



