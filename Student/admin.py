from django.contrib import admin
from django.utils.html import format_html
from .models import Seven_Student_One, Seven_Student_Two, Eight_Student_One, Eight_Student_Two, Nine_Student_One, Nine_Student_Two

class Seven_Student_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Seven_Student_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Eight_Student_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'


class Eight_Student_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'


class Nine_Student_One_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



class Nine_Student_Two_Admin(admin.ModelAdmin):
    list_display = ('name', 'username', 'father_name', 'display_photo', 'password_display', 'father_Phone')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return "No Photo"
    display_photo.short_description = 'Photo'


    def password_display(self, obj):
        return '********'
    password_display.short_description = 'Password'



admin.site.register(Seven_Student_One, Seven_Student_One_Admin)
admin.site.register(Seven_Student_Two, Seven_Student_Two_Admin)
admin.site.register(Eight_Student_One, Eight_Student_One_Admin)
admin.site.register(Eight_Student_Two, Eight_Student_Two_Admin)
admin.site.register(Nine_Student_One, Nine_Student_One_Admin)
admin.site.register(Nine_Student_Two, Nine_Student_Two_Admin)