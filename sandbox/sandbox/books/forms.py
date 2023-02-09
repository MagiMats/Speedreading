from django.forms import ModelChoiceField, ModelForm

from .models import Book

import fitz

class UserChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class BookUploadForm(ModelForm):    
    class Meta:
        model = Book
        fields = ['title', 'book_file']
