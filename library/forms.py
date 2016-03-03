from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text='Nombre autor: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Author
		fields = ('name',)