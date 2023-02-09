from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegisterForm, LoginForm

# Create your views here.
def register_view(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():            
            form.save()
            return HttpResponse('SUCCES')

        context['messages'] = "Invalid register"

    else:
        form = UserRegisterForm()

    context['form'] = form
    return render(request, 'auth/register.html', context)

def login_view(request):
    context = {}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('books:index'))
    
    context["form"] = LoginForm()
    return render(request, 'auth/login.html', context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('users:login'))
    
