from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import BaseUser
from library.models import Book
from book_borrows.models import Borrow

def in_base_user_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and user.groups.filter(name='usuario_base').exists()


def index(request):
	context = {}
	return render(request, 'website/index.html', context)


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		if user:	
			if user.groups.filter(name='usuario_base').exists():
				login(request, user)
				return redirect('website:book_list')
			else:
				messages.error(request, 'La cuenta de usuario debe existir para poder ingresar')
	context = {}
	return render(request, 'website/login.html', context)


@user_passes_test(in_base_user_group, login_url = 'website:login')
def book_list(request):
	books = Book.objects.all().order_by('name') 
	search = '¿Qué es lo que buscas?'
	if request.method == 'GET':
		search_text = request.GET.get('search-text', None)
		search_class = request.GET.get('search-class', None)
		search = search_text		
		if search_class == 'Book':
			books = Book.objects.filter(name__icontains=search_text).order_by('name')	
		elif search_class == 'Author':
			books = Book.objects.filter(authors__icontains=search_text).order_by('name')
		elif search_class == 'Category':
			books = Book.objects.filter(categories__icontains=search_text).order_by('name')
	context = {
		'books': books,
		'search': search,
	}
	return render(request, 'website/book_list.html', context)


@user_passes_test(in_base_user_group, login_url = 'website:login')
def my_borrows(request):
	current_user = BaseUser.objects.get(user=request.user)
	borrows = Borrow.objects.filter(user=current_user)	
	for borrow in borrows:
		if timezone.now().date() > borrow.end_date.date() and borrow.status != 'RE':
			Borrow.objects.filter(pk=borrow.pk).update(status='EX')
	context = {
		'borrows': borrows,
	}
	return render(request, 'website/my_borrows.html', context)

