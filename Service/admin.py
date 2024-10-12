from django.contrib import admin
from .models import Service

class Service_Admin(admin.ModelAdmin):
    list_display = ('service_name', 'service_description')

admin.site.register(Service, Service_Admin)