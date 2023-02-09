from django.db import models
import fitz

class Book(models.Model):
    page_amount = models.IntegerField(default='0')    
    title = models.CharField(max_length=200)

    book_file = models.FileField(upload_to='books', null=True)
    file_text = models.TextField(null=True)
