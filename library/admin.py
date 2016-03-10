from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ('name',)

