from django.contrib import admin
from . models import *

admin.site.register(MovieCollection)
admin.site.register(Genrie)
admin.site.register(Countrie)
admin.site.register(Voice)
admin.site.register(Profile)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor', 'date', 'img')
    search_fields = ('actor', )
    list_per_page = 30


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('director', 'date', 'img')
    search_fields = ('director', )
    list_per_page = 30


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title_eng', 'title_geo', 'type', 'img')
    search_fields = ('title_eng', 'title_geo')
    list_per_page = 30
    # list_filter = ('type')
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Comment)
