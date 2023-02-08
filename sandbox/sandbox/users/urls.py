from django.urls import path
from .views import RegisterView, logout_view, login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]
