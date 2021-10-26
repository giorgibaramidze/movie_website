from django.contrib import admin
from . models import *

admin.site.register(Genrie)
admin.site.register(Actor)
admin.site.register(Countrie)
admin.site.register(Voice)
admin.site.register(Director)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title_eng', 'title_geo', 'type', 'img')
admin.site.register(Movie, MovieAdmin)
