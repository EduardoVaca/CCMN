from django import forms
from .models import Author, Category


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