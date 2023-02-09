from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.contrib.auth import get_user_model, logout, views, login, authenticate
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import MyUser
from .forms import UserCreationForm, LoginForm

# Create your views here.
class RegisterView(CreateView):
    model = MyUser
    template_name = 'users/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        return HttpResponseRedirect(reverse_lazy('users:login'))

def login_view(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            
            if user is not None:        
                login(request, user)
                return HttpResponseRedirect('books:index')
                
            else:
                message = 'Login failed!'
        
    return render(request, 'users/login.html', context={'form': form, 'message': message})

def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('users:login')

