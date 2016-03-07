from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^administrador/author/$', views.author_list, name='author_list'),
	url(r'^administrador/author/add$', views.author_add, name='author_add'),
	url(r'^administrador/author/delete/(?P<pk>[0-9]+)/$', views.author_delete, name='author_delete'),
	url(r'^administrador/category/$', views.category_list, name='category_list'),
	url(r'^administrador/category/add/$', views.category_add, name='category_add'),
]