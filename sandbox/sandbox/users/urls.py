from django.urls import path
from .views import MyLoginView, RegisterView, logout_view

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]
