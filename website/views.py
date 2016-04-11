from django.shortcuts import render


def index(request):
	context = {}
	return render(request, 'website/index.html', context)


def login(request):
	context = {}
	return render(request, 'website/login.html', context)
