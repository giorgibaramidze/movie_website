from django.contrib import admin
from . models import *

admin.site.register(Genrie)
admin.site.register(Actor)
admin.site.register(Countrie)
admin.site.register(Voice)
admin.site.register(Director)
admin.site.register(Profile)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title_eng', 'title_geo', 'type', 'img')
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
