import datetime

from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Borrow
from library.models import Book
from users.models import BaseUser


def in_admin_group(user):
    """Use with a ``user_passes_test`` decorator to restrict access to 
    authenticated users who are not in the "administrator" group."""
    return user.is_authenticated() and (user.is_superuser or user.groups.filter(name='administrator').exists())


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def borrow_list(request):
	borrows = Borrow.objects.all()
	for borrow in borrows:
		if timezone.now().date() > borrow.end_date.date() and borrow.status != 'RE':
			Borrow.objects.filter(pk=borrow.pk).update(status='EX')
	borrows = Borrow.objects.all()
	context = {
		'borrows': borrows,
	}
	return render(request, 'administrador/borrow_list.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def borrow_add(request):
	if request.method == 'POST':
		user_pk = request.POST.get('user')
		user = get_object_or_404(BaseUser, pk=user_pk)
		book_pk = request.POST.get('book')
		book = get_object_or_404(Book, pk=book_pk)
		date_str = request.POST.get('end_date')
		end_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
		Borrow.objects.create(user=user, book=book, end_date=end_date)
		Book.objects.filter(pk=book_pk).update(book_status='BO')
		return redirect('book_borrows:borrow_list')

	books = Book.objects.filter(book_status='AV')
	users = BaseUser.objects.all()
	context = {
		'books': books,
		'users': users,
	}
	return render(request, 'administrador/borrow_add.html', context)


@user_passes_test(in_admin_group, login_url = 'admin_users:authentication')
def borrow_return(request, pk):
	Borrow.objects.filter(pk=pk).update(status='RE')
	borrow = get_object_or_404(Borrow, pk=pk)
	Book.objects.filter(pk=borrow.book.pk).update(book_status='AV')	
	return redirect('book_borrows:borrow_list')

