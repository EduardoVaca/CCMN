from django.conf.urls import url

from . import views

urlpatterns = [	
	url(r'^login/$', views.user_login, name='login'),
	url(r'^lectura/$', views.book_list, name='book_list'),
	url(r'^$', views.index, name='index'),
]