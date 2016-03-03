from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test


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
		return redirect('/')

	context = {}
	return render(request, 'administrador/login.html', context)


@user_passes_test(in_admin_group, login_url = 'login/')
def dashboard(request):
	context = {}
	return render(request, 'administrador/dashboard.html', context)

