# Generated by Django 4.0.3 on 2022-03-05 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0003_books_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image',
        ),
    ]
