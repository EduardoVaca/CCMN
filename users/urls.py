from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.auth_login, name='authentication'),
	url(r'^$', views.dashboard, name='dashboard'),
]