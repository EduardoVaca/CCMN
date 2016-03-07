from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Author, Category
from .forms import AuthorForm, CategoryForm


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
