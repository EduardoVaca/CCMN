from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^login/$', views.auth_login, name='authentication'),
	url(r'^users-admin/add/$', views.add_user_admin, name='add_user_admin'),
	url(r'^users_admin/delete/(?P<pk>[0-9]+)/$', views.delete_user_admin, name='delete_user_admin'),
	url(r'^users-admin/logout/$', auth_views.logout, {'next_page': 'admin_users:authentication'}, name='logout'),
	url(r'^users-admin/$', views.users_admin, name='users_admin'),
	url(r'^base-user/$', views.base_user_list, name='base_user_list'),
	url(r'^base-user/add/$', views.base_user_add, name='base_user_add'),		
	url(r'^$', views.dashboard, name='dashboard'),
]