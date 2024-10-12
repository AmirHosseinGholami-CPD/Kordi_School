from django.contrib import admin
from .models import Common

class Common_Admin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Common, Common_Admin)
