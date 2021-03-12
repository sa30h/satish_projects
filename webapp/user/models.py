from django.db import models

# Create your models here.
class Worker(models.Model):
    
    username=models.CharField(max_length=40)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=15)
