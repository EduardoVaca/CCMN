from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

from .models import AdminUser, BaseUser
from library.models import Book, Author, Category
from book_borrows.models import Borrow


def in_admin_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and (user.is_superuser or user.groups.filter(name='administrator').exists())


def auth_login(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		if user:	
			if user.groups.filter(name='administrator').exists() or user.is_superuser:
				login(request, user)
				return redirect('admin_users:dashboard')

	context = {}
	return render(request, 'administrador/login.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def dashboard(request):
	books_num = Book.objects.all().count()
	authors_num = Author.objects.all().count()
	categories_num = Category.objects.all().count()
	users = BaseUser.objects.all().count()
	borrowed = Borrow.objects.filter(status='BO').count()
	expired = Borrow.objects.filter(status='EX').count()
	context = {
		'books_num': books_num,
		'authors_num': authors_num,
		'categories_num': categories_num,
		'users_num': users,
		'borrowed_num': borrowed,
		'expired_num': expired,
	}
	return render(request, 'administrador/dashboard.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def users_admin(request):	
	admin_users = AdminUser.objects.all().order_by('user')	
	context = {
		'admin_users': admin_users,			
	}
	return render(request, 'administrador/user_administrador_lista.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def add_user_admin(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user, created = User.objects.get_or_create(username=username)
		user.set_password(password)
		user.save()		
		admin_user = AdminUser.objects.create(user=user)		
		admin_user.save()
		messages.success(request, 'El administrador se ha agregado con éxito')
		return redirect('admin_users:users_admin')
	else:
		context = {}
		return render(request, 'administrador/add_admin_user.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def delete_user_admin(request, pk):
	admin_user = get_object_or_404(AdminUser, pk = pk)
	admin_user.user.delete()
	admin_user.delete()
	messages.success(request, 'El administrador se ha eliminado con éxito')
	return redirect('admin_users:users_admin')


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def base_user_list(request):
	base_users = BaseUser.objects.all().order_by('last_name')
	context = {
		'base_users': base_users,
	}
	return render(request, 'administrador/base_users_list.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def base_user_add(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		last_name = request.POST.get('last_name', None)
		email = request.POST.get('email', None)
		age = request.POST.get('age', None)
		sex = request.POST.get('sex', None)
		phone = request.POST.get('number', None)
		password = request.POST.get('password', None)
		address = request.POST.get('address', None)
		user, created = User.objects.get_or_create(username=email)
		user.set_password(password)
		user.save()
		BaseUser.objects.create(user=user,
								name=name,
								last_name=last_name,
								age=age,
								sex=sex,
								phone=phone,
								address=address)
		messages.success(request, 'El usuario se ha guardado con éxito')
		return redirect('admin_users:base_user_list')

	context = {}
	return render(request, 'administrador/base_user_add.html', context)







