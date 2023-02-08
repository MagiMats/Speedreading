from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.contrib.auth import get_user_model, logout, views, login, authenticate
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreationForm, LoginForm

# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect(reverse_lazy('users:login'))

def login_view(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('valid')
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            print(user)
            
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('home')
        message = 'Login failed!'
        
    return render(request, 'users/login.html', context={'form': form, 'message': message})

def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('users:login')

