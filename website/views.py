from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import BaseUser

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
	context = {}
	return render(request, 'website/book_list.html', context)
