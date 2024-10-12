from django.contrib import admin
from .models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)

class BaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'lessone']

admin.site.register(Seven_One_Absence, BaseAdmin)
admin.site.register(Seven_Two_Absence, BaseAdmin)
admin.site.register(Eight_One_Absence, BaseAdmin)
admin.site.register(Eight_Two_Absence, BaseAdmin)
admin.site.register(Nine_One_Absence, BaseAdmin)
admin.site.register(Nine_Two_Absence, BaseAdmin)