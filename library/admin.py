from django.contrib import admin
from .models import Book, Author, Category, Wrote, Has

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Wrote)
class AdminWrote(admin.ModelAdmin):
	list_display = ('author', 'book',)

@admin.register(Has)
class AdminHas(admin.ModelAdmin):
	list_display = ('book', 'category',)
