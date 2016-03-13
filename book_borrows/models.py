from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from library.models import Book
from users.models import BaseUser


class Borrow(models.Model):
	user = models.ForeignKey(BaseUser)
	book = models.ForeignKey(Book)

	start_date = models.DateTimeField(default=timezone.now)
	end_date = models.DateTimeField(null=False)

	STATUS_RETURNED = 'RE'
	STATUS_BORROWED = 'BO'
	STATUS_EXIPRED = 'EX'

	status_choices = (
			(STATUS_RETURNED, 'Regresado'),
			(STATUS_BORROWED, 'En Préstamo'),
			(STATUS_EXIPRED, 'Vencido'),
		)
	status = models.CharField(max_length=2,
								choices=status_choices,
								default='BO')

	def save(self, *args, **kwargs):
		if self.start_date < self.end_date:
			super().save(*args, **kwargs)
		else:
			raise ValidationError('Book borrow cannot end before it begins')

	class Meta:
		verbose_name_plural='borrows'
