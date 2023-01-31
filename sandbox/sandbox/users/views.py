from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, logout, views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.
class RegisterView(View):
    template_name = 'users/register.html'
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        message = ''

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('VALID')
            user = form.save()

            if user is not None:            
                return reverse_lazy('users:login') 

        message = 'Sign up failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('books:index') 
    
    def form_invalid(self, form):
        print('not a valid person')
        return self.render_to_response(self.get_context_data(form=form))
    

def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('/')

