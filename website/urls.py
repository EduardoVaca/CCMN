from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [	
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'website:login'}, name='logout'),
	url(r'^lectura/$', views.book_list, name='book_list'),
	url(r'^$', views.index, name='index'),	
]