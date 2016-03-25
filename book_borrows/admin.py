from django.contrib import admin
from .models import Borrow

@admin.register(Borrow)
class AdminBook(admin.ModelAdmin):
	list_display = ('user', 'book', 'start_date', 'end_date')
