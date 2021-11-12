from django.contrib import admin
from . models import *

admin.site.register(MovieCollection)
admin.site.register(Genrie)
admin.site.register(Actor)
admin.site.register(Countrie)
admin.site.register(Voice)
admin.site.register(Director)
admin.site.register(Profile)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title_eng', 'title_geo', 'type', 'img')
    search_fields = ('title_eng', 'title_geo')
    list_per_page = 30
    # list_filter = ('type')
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
