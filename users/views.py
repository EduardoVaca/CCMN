from django.shortcuts import render


def auth_login(request):
	context = {}
	return render(request, 'admin/login.html', context)
