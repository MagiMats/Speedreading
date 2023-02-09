from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    page_amount = models.IntegerField(default='0')
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    book_file = models.FileField(upload_to='books', null=True)
    file_text = models.TextField(null=True)