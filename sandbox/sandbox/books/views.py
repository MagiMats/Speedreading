from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from books.models import Book
from .forms import BookUploadForm
from .functions import parse_pdf_to_text_array

import json
import numpy as np

class BookLoginMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'login'

class BookListView(LoginRequiredMixin, ListView):
    login_url = '/users/login/'
    
    model = Book
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user = request.user

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.user.username
        context['object_list'] = context['object_list'][0:self.user.book_amount]
        return context

class BookDetailView(DetailView, LoginRequiredMixin):
    model = Book

class OnLoadGetBookTextDetailView(DetailView, LoginRequiredMixin):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_file = kwargs['object'].book_file        
        context['book_list_text'] = parse_pdf_to_text_array(book_file)

        return context

class BookJsonDetailView(DetailView, LoginRequiredMixin):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_file = kwargs['object'].book_file        
        book_text_array = parse_pdf_to_text_array(book_file)

        context['book_json'] = json.dumps(book_text_array) 
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
    instance.file_text = parse_pdf_to_text_array(instance.book_file)
    instance.save()

def succes_view(request):
    return render(request, 'books/succes.html')