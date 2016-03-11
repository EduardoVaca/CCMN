from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^administrador/author/$', views.author_list, name='author_list'),
	url(r'^administrador/author/add$', views.author_add, name='author_add'),
	url(r'^administrador/author/delete/(?P<pk>[0-9]+)/$', views.author_delete, name='author_delete'),
	url(r'^administrador/author/update/(?P<pk>[0-9]+)/$', views.author_update, name='author_update'),	
	url(r'^administrador/category/add/$', views.category_add, name='category_add'),
	url(r'^administrador/category/delete/(?P<pk>[0-9]+)/$', views.category_delete, name='category_delete'),
	url(r'^administrador/category/$', views.category_list, name='category_list'),
	url(r'^administrador/book/add/$', views.book_add, name='book_add'),
	url(r'^administrador/book/$', views.book_list, name='book_list'),
]