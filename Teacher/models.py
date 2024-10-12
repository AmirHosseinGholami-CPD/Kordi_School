from django.db import models
from django.contrib.auth.models import User

class Seven_Teacher_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name
    

class Seven_Teacher_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name

class Eight_Teacher_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name

class Eight_Teacher_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name

class Nine_Teacher_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name

class Nine_Teacher_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.name
