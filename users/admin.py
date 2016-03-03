from django.contrib import admin
from .models import AdminUser

@admin.register(AdminUser)
class AdminHas(admin.ModelAdmin):
	list_display = ('user',)
