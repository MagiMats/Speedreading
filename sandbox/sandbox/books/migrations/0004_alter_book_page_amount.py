# Generated by Django 4.1.5 on 2023-01-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_amount',
            field=models.IntegerField(default='0'),
        ),
    ]
