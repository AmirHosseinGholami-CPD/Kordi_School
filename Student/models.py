from django.db import models

class Seven_Student_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username

class Seven_Student_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username

class Eight_Student_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username

class Eight_Student_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username

class Nine_Student_One(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username

class Nine_Student_Two(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    father_Phone = models.CharField(max_length=128)
    Mother_Phone = models.CharField(max_length=128)
    born = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username