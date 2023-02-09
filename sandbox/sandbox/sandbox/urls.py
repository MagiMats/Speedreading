from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include(('books.urls', 'home'), namespace='home')),
    path('books/', include(('books.urls', 'books'), namespace='books')),
    path('users/', include(('custom_users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)