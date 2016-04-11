from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls', namespace='admin_users')),
    url(r'^', include('library.urls', namespace='library')),
    url(r'^', include('book_borrows.urls', namespace='book_borrows')),    
]
