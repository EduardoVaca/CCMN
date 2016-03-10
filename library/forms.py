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

	# Representing the many to many related fields in Book
	authors = forms.ModelMultipleChoiceField(help_text='Autores: ', queryset=Author.objects.all(), required=True)
	categories = forms.ModelMultipleChoiceField(help_text='Categorías: ', queryset=Category.objects.all(), required=True)

	# Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
	# def __init__(self, *args, **kwargs):
	# 	if kwargs.get('instance'):
	# 		# We get the 'initial' keyword argument or initialize it
 #            # as a dict if it didn't exist.
	# 		initial = kwargs.setdefault('initial', {})
 #            # The widget for a ModelMultipleChoiceField expects
 #            # a list of primary key for the selected data.
	# 		initial['authors'] = [author.pk for author in kwargs['instance'].author_set.all()]
	# 		initial['categories'] = [category.pk for category in kwargs['instance'].category_set.all()]

	# 	forms.ModelForm.__init__(self, *args, **kwargs)

	# def save(self):
	# 	instance = forms.ModelForm.save(self)
	# 	instance.author_set.clear()
	# 	instance.category_set.clear()
	# 	for author in self.cleaned_data['authors']:
	# 		instance.author_set.add(author)
	# 	for category in self.cleaned_data['categories']:
	# 		instance.category_set.add(category)

	class Meta:
		model = Book
		fields = ('name', 'authors', 'categories',)

