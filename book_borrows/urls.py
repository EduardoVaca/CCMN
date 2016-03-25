from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^administrador/borrow/$', views.borrow_list, name='borrow_list'),
]