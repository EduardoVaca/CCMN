from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def auth_login(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/')

	context = {}
	return render(request, 'admin/login.html', context)


def dashboard(request):
	context = {}
	return render(request, 'admin/dashboard.html', context)

