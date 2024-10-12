from django.contrib import admin
from django.utils.html import format_html
from .models import Staff

class Staff_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'staff', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'


admin.site.register(Staff, Staff_Admin)