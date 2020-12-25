from django.db import models


# Create your models here.
class Book(models.Model):
    bookname=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    booktype=models.CharField(max_length=20)

    
