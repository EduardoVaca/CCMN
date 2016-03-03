from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^administrador/author/$', views.author_list, name='author_list'),
]