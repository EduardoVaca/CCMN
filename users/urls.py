from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^login/$', views.auth_login, name='authentication'),
	url(r'^users-admin/add/$', views.add_user_admin, name='add_user_admin'),
	url(r'^users_admin/delete/(?P<pk>[0-9]+)/$', views.delete_user_admin, name='delete_user_admin'),
	url(r'^users-admin/logout/$', auth_views.logout, {'next_page': 'admin_users:authentication'}, name='logout'),
	url(r'^users-admin/$', views.users_admin, name='users_admin'),		
	url(r'^$', views.dashboard, name='dashboard'),
]