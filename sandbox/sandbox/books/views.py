from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from books.models import Book
from .forms import BookUploadForm
from .functions import parse_text

class BookLoginMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'login'

class BookListView(LoginRequiredMixin, ListView):
    login_url = 'users/login/'
    
    model = Book
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.username = request.user.username

    def get_context_data(self, **kwargs):    
        context = {
            'user_name': self.username,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

class BookDetailView(DetailView, LoginRequiredMixin):
    model = Book

class OnLoadGetBookTextDetailView(DetailView, LoginRequiredMixin):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_file = kwargs['object'].book_file        
        context['book_text'] = parse_text(book_file)
        
        return context

def upload_book_file_view(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)

        if form.is_valid():
            parse_book_file(request, form)
            return HttpResponseRedirect('succes')
    else:
        form = BookUploadForm()
    return render(request, 'books/book_upload.html', {'form': form})

def parse_book_file(request, form):
    instance = form.save(commit = False)
    instance.book_file = request.FILES['book_file']
    instance.save()
    instance.file_text = parse_text(instance.book_file)
    instance.save()

def succes_view(request):
    return render(request, 'books/succes.html')