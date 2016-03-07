from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^administrador/', include('users.urls', namespace='admin_users')),
    url(r'^', include('library.urls', namespace='library')),
]
