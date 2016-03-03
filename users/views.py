from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import AdminUser


def in_admin_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and (user.is_superuser or user.groups.filter(name='administrador').exists())


def auth_login(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('admin_users:dashboard')

	context = {}
	return render(request, 'administrador/login.html', context)


@user_passes_test(in_admin_group, login_url = 'login/')
def dashboard(request):
	context = {}
	return render(request, 'administrador/dashboard.html', context)


@user_passes_test(in_admin_group, login_url = 'login/')
def users_admin(request):
	context = {}
	return render(request, 'administrador/user_administrador_lista.html', context)


@user_passes_test(in_admin_group, login_url = 'login/')
def add_user_admin(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = User.objects.create(username=username, password=password)
		admin_user = AdminUser.objects.create(user=user)
		admin_user.save()
		return redirect('admin_users:users_admin')
	else:
		context = {}
		return render(request, 'administrador/add_admin_user.html', context)



