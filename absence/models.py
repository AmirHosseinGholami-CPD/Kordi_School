from django.db import models

class Seven_One_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"

class Seven_Two_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"

class Eight_One_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"

class Eight_Two_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"

class Nine_One_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"

class Nine_Two_Absence(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=50)
    lessone = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.day}: {self.lessone}"