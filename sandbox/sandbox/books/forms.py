from django.forms import ModelChoiceField, ModelForm

from .models import Book, Author

class UserChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class BookUploadForm(ModelForm):
    author = UserChoiceField(Author.objects.all())
    class Meta:
        model = Book
        fields = ['author', 'title', 'book_file']
