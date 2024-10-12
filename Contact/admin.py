from django.contrib import admin
from .models import Contact
class Contact_Admin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'message')

admin.site.register(Contact, Contact_Admin)