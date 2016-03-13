from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Author, Category, Book, Wrote, Has
from .forms import AuthorForm, CategoryForm, BookForm


def in_admin_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and (user.is_superuser or user.groups.filter(name='administrator').exists())


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def author_list(request):
	authors = Author.objects.all().order_by('name')
	context = {
		'authors': authors,
	}
	return render(request, 'administrador/author_list.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def author_add(request):
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			author = form.save()
			author.save()
			return redirect('library:author_list')
	else:
		form = AuthorForm()
	context = {
		'authorForm': form,
	}
	return render(request, 'administrador/add_author.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def author_update(request, pk):
	current_author = get_object_or_404(Author, pk=pk)
	if request.method == 'POST':		
		form = AuthorForm(request.POST or None, instance=current_author)
		if form.is_valid():
			form.save()
			return redirect('library:author_list')
	else:
		form = AuthorForm(instance=current_author)
	context = {
		'authorForm': form,
	}
	return render(request, 'administrador/add_author.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def author_delete(request, pk):
	author = get_object_or_404(Author, pk=pk)
	author.delete()	
	return redirect('library:author_list')


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def category_list(request):
	categories = Category.objects.all().order_by('name')
	context = {
		'categories': categories,
	}
	return render(request, 'administrador/category_list.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def category_add(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save()
			category.save()
			return redirect('library:category_list')
	else:
		form = CategoryForm()
	context = {
		'categoryForm': form,
	}
	return render(request, 'administrador/category_add.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def category_delete(request, pk):
	category = get_object_or_404(Category, pk=pk)
	category.delete()
	return redirect('library:category_list')


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def book_list(request):
	books = Book.objects.all().order_by('name')
	context = {
		'books': books,
	}
	return render(request, 'administrador/book_list.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def book_add(request):	
	if request.method == 'POST':
		name = request.POST.get('name_book')
		authors = request.POST.getlist('author')
		categories = request.POST.getlist('category')
		book = Book.objects.create(name=name)
		for author in authors:
			current_author = Author.objects.get(pk=author)
			Wrote.objects.create(author=current_author, book=book)
		for category in categories:
			current_category = Category.objects.get(pk=category)
			Has.objects.create(book=book, category=current_category)
		return redirect('library:book_list')

	authors = Author.objects.all().order_by('name')
	categories = Category.objects.all().order_by('name')
	context = {
		'authors': authors,
		'categories': categories,
	}
	return render(request, 'administrador/book_add.html', context)
