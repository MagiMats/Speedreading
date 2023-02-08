from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.contrib.auth import get_user_model, logout, views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import User

# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        return HttpReponseRedirect(reverse_lazy('users:login'))

class MyLoginView(views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return HttpReponseRedirect(reverse_lazy('index'))
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        print(self.request)
        return self.render_to_response(self.get_context_data(form=form))

def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('/')

