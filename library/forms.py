from django import forms
from .models import Author, Category, Book


class AuthorForm(forms.ModelForm):
	name = forms.CharField(max_length=255, help_text='Nombre autor: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Author
		fields = ('name',)


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=255, help_text='Nombre categoría: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Category
		fields = ('name',)


class BookForm(forms.ModelForm):
	name = forms.CharField(max_length=255, help_text='Nombre libro: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	authors = forms.ModelMultipleChoiceField(help_text='Autores: ', queryset=Author.objects.all(), required=True, \
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'select2_single form-control'}))
	categories = forms.ModelMultipleChoiceField(help_text='Autores: ', queryset=Category.objects.all(), required=True, \
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'select2_single form-control'}))

	class Meta:
		model = Book
		fields = ('name', 'authors', 'categories',)
    