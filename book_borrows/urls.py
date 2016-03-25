from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^administrador/borrow/$', views.borrow_list, name='borrow_list'),
	url(r'^administrador/borrow/add/$', views.borrow_add, name='borrow_add'),
	url(r'^administrador/borrow/return/(?P<pk>[0-9]+)/$', views.borrow_return, name='borrow_return'),
]