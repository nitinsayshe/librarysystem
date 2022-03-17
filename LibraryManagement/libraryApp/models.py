from django.db import models
import datetime
import os

# Create your models here.



class Books(models.Model):
    bookName=models.CharField(max_length=30)
    bookPrice=models.PositiveIntegerField()
    bookAuthor=models.CharField(max_length=30)
    bookSummary=models.TextField(max_length=150)





