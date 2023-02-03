from django.urls import path
from .views import (
    BookListView, 
    BookDetailView,
    OnLoadGetBookTextDetailView,
    upload_book_file_view, 
    succes_view,
    BookJsonDetailView,
    )

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<int:pk>/', BookJsonDetailView.as_view(), name='detail'),
    path('upload', upload_book_file_view, name='upload_book'),
    path('succes', succes_view,)
]