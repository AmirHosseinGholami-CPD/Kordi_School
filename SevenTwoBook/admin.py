from django.contrib import admin
from .models import (
    Fizik, Shimi, Zist,
    Math, Farsi, Emla,
    Negaresh, English,
    Arabic, Quran, Maref,
    Kar_Fan, Computer, Motaleat,
    Tafakor, Farhang_Honar, Varzesh
)

class Lessone(admin.ModelAdmin):
    list_display = ['name', 'month', 'score']

admin.site.register(Fizik, Lessone)
admin.site.register(Shimi, Lessone)
admin.site.register(Zist, Lessone)
admin.site.register(Math, Lessone)
admin.site.register(Farsi, Lessone)
admin.site.register(Emla, Lessone)
admin.site.register(Negaresh, Lessone)
admin.site.register(English, Lessone)
admin.site.register(Arabic, Lessone)
admin.site.register(Quran, Lessone)
admin.site.register(Maref, Lessone)
admin.site.register(Kar_Fan, Lessone)
admin.site.register(Computer, Lessone)
admin.site.register(Motaleat, Lessone)
admin.site.register(Tafakor, Lessone)
admin.site.register(Farhang_Honar, Lessone)
admin.site.register(Varzesh, Lessone)