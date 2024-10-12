from django.db import models

class Fizik(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Shimi(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Zist(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Math(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Farsi(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Emla(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Negaresh(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class English(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Arabic(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Quran(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Maref(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Kar_Fan(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Computer(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Motaleat(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Tafakor(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Farhang_Honar(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"

class Varzesh(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}: {self.score}"