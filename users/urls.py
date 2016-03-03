from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.auth_login, name='authentication'),
	url(r'^users-admin/add/$', views.add_user_admin, name='add_user_admin'),
	url(r'^users-admin/$', views.users_admin, name='users_admin'),	
	url(r'^$', views.dashboard, name='dashboard'),
]