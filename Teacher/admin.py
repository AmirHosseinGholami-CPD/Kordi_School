from django.contrib import admin
from django.utils.html import format_html
from .models import Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One, Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two

class Seven_Teacher_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Seven_Teacher_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Eight_Teacher_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'


class Eight_Teacher_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'


class Nine_Teacher_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Nine_Teacher_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'phone_number', 'course', 'display_photo', 'password_display')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



admin.site.register(Seven_Teacher_One, Seven_Teacher_One_Admin)
admin.site.register(Seven_Teacher_Two, Seven_Teacher_Two_Admin)
admin.site.register(Eight_Teacher_One, Eight_Teacher_One_Admin)
admin.site.register(Eight_Teacher_Two, Eight_Teacher_Two_Admin)
admin.site.register(Nine_Teacher_One, Nine_Teacher_One_Admin)
admin.site.register(Nine_Teacher_Two, Nine_Teacher_Two_Admin)