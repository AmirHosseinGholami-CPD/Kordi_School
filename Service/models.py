from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()

    def __str__(self):
        return self.service_name
