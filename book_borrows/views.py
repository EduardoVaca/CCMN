from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from . models import Borrow


def in_admin_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and (user.is_superuser or user.groups.filter(name='administrator').exists())


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def borrow_list(request):
	borrows = Borrow.objects.all()
	context = {
		'borrows': borrows,
	}
	return render(request, 'administrador/borrow_list.html', context)


