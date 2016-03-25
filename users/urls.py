from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^administrador/login/$', views.auth_login, name='authentication'),
	url(r'^administrador/users-admin/add/$', views.add_user_admin, name='add_user_admin'),
	url(r'^administrador/users_admin/delete/(?P<pk>[0-9]+)/$', views.delete_user_admin, name='delete_user_admin'),
	url(r'^administrador/users-admin/logout/$', auth_views.logout, {'next_page': 'admin_users:authentication'}, name='logout'),
	url(r'^administrador/users-admin/$', views.users_admin, name='users_admin'),
	url(r'^administrador/base-user/$', views.base_user_list, name='base_user_list'),
	url(r'^administrador/base-user/add/$', views.base_user_add, name='base_user_add'),		
	url(r'^administrador/$', views.dashboard, name='dashboard'),
]