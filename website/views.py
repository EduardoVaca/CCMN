from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from users.models import BaseUser

def in_base_user_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and user.groups.filter(name='usuario_base').exists()


def index(request):
	context = {}
	return render(request, 'website/index.html', context)


def login(request):
	context = {}
	return render(request, 'website/login.html', context)


@user_passes_test(in_base_user_group, login_url = 'website:login')
def book_list(request): 
	context = {}
	return render(request, 'website/book_list.html', context)
